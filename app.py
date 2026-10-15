"""Aplicación de escritorio del Sistema Experto Educativo.

Ejecuta: python3 app.py
"""
try:
    import tkinter.messagebox as messagebox
    import customtkinter as ctk
except ModuleNotFoundError as error:
    if error.name == "_tkinter":
        raise SystemExit(
            "Este Python no incluye Tk. Instala una distribución de Python con Tcl/Tk "
            "o el paquete tkinter de tu sistema y vuelve a ejecutar la aplicación."
        ) from error
    raise SystemExit("Falta CustomTkinter. Instálalo con: python3 -m pip install -r requirements.txt") from error

from cuestionario import SECCIONES
from evaluacion import evaluar_perfil


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class SistemaExpertoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("OrientaU | Sistema Experto Educativo")
        self.geometry("1080x760")
        self.minsize(920, 650)
        self.hechos = {}
        self.respuestas = {}
        self.indice_seccion = -1
        self.comentario = None
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self._encabezado()
        self.contenido = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.contenido.grid(row=1, column=0, sticky="nsew", padx=34, pady=(0, 24))
        self.mostrar_bienvenida()

    def _encabezado(self):
        barra = ctk.CTkFrame(self, height=88, corner_radius=0)
        barra.grid(row=0, column=0, sticky="ew")
        barra.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(barra, text="OrientaU", font=ctk.CTkFont(size=28, weight="bold")).grid(
            row=0, column=0, sticky="w", padx=34, pady=(15, 0))
        self.estado = ctk.CTkLabel(barra, text="Sistema experto de orientación académica", text_color=("#53606d", "#bdc5cf"))
        self.estado.grid(row=1, column=0, sticky="w", padx=34, pady=(0, 14))

    def limpiar(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_bienvenida(self):
        self.limpiar()
        self.estado.configure(text="Antes de comenzar")
        tarjeta = ctk.CTkFrame(self.contenido, corner_radius=18)
        tarjeta.place(relx=.5, rely=.5, anchor="center", relwidth=.82, relheight=.78)
        ctk.CTkLabel(tarjeta, text="Conoce los factores detrás de tu rendimiento", font=ctk.CTkFont(size=29, weight="bold"), wraplength=680).pack(padx=40, pady=(55, 16))
        texto = (
            "Este sistema analiza hábitos de estudio, tiempo disponible, entorno, evaluación y apoyo académico. "
            "Su finalidad es identificar prioridades y ofrecer acciones concretas para mejorar tu situación.\n\n"
            "No sustituye una evaluación psicológica, médica ni una asesoría institucional. Tus respuestas no se guardan automáticamente."
        )
        ctk.CTkLabel(tarjeta, text=texto, justify="left", wraplength=680, font=ctk.CTkFont(size=16), text_color=("#3e4a57", "#d1d7dd")).pack(padx=48, pady=12)
        ctk.CTkButton(tarjeta, text="Comenzar evaluación", height=46, font=ctk.CTkFont(size=16, weight="bold"), command=lambda: self.mostrar_seccion(0)).pack(pady=(28, 45))

    def mostrar_seccion(self, indice):
        self.indice_seccion = indice
        self.limpiar()
        nombre, preguntas = SECCIONES[indice]
        self.estado.configure(text=f"Sección {indice + 1} de {len(SECCIONES)} · {nombre}")
        progreso = ctk.CTkProgressBar(self.contenido)
        progreso.pack(fill="x", pady=(4, 12))
        progreso.set((indice + 1) / len(SECCIONES))
        ctk.CTkLabel(self.contenido, text=nombre, font=ctk.CTkFont(size=25, weight="bold")).pack(anchor="w", pady=(0, 4))
        ctk.CTkLabel(self.contenido, text="Responde según tu situación actual. Todos los campos son obligatorios.", text_color=("#586776", "#b8c2cb")).pack(anchor="w", pady=(0, 12))
        formulario = ctk.CTkScrollableFrame(self.contenido, corner_radius=14)
        formulario.pack(fill="both", expand=True)
        for clave, pregunta, tipo, datos, ayuda in preguntas:
            bloque = ctk.CTkFrame(formulario, fg_color="transparent")
            bloque.pack(fill="x", padx=16, pady=12)
            ctk.CTkLabel(bloque, text=pregunta, anchor="w", font=ctk.CTkFont(size=16, weight="bold")).pack(fill="x")
            if ayuda:
                ctk.CTkLabel(bloque, text=ayuda, anchor="w", text_color=("#627080", "#a9b4bf")).pack(fill="x", pady=(2, 5))
            if tipo == "numero":
                variable = self.respuestas.get(clave) or ctk.StringVar(value=str(self.hechos.get(clave, "")))
                self.respuestas[clave] = variable
                entrada = ctk.CTkEntry(bloque, textvariable=variable, placeholder_text=f"Entre {datos} y {ayuda and '100' or ''}", width=220)
                entrada.pack(anchor="w", pady=(4, 0))
                entrada.configure(placeholder_text="Escribe un número")
            else:
                variable = self.respuestas.get(clave) or ctk.StringVar(value=self.hechos.get(clave, ""))
                self.respuestas[clave] = variable
                opciones = ctk.CTkFrame(bloque, fg_color="transparent")
                opciones.pack(fill="x", pady=(5, 0))
                for texto, valor in datos:
                    ctk.CTkRadioButton(opciones, text=texto, variable=variable, value=valor).pack(side="left", padx=(0, 22), pady=3)
        controles = ctk.CTkFrame(self.contenido, fg_color="transparent")
        controles.pack(fill="x", pady=(13, 0))
        if indice:
            ctk.CTkButton(controles, text="← Anterior", fg_color="transparent", border_width=1, command=lambda: self.mostrar_seccion(indice - 1)).pack(side="left")
        texto_boton = "Continuar →" if indice < len(SECCIONES) - 1 else "Continuar al comentario →"
        ctk.CTkButton(controles, text=texto_boton, command=self.guardar_y_continuar).pack(side="right")

    def guardar_y_continuar(self):
        _, preguntas = SECCIONES[self.indice_seccion]
        for clave, _, tipo, datos, _ in preguntas:
            valor = self.respuestas[clave].get().strip()
            if not valor:
                return messagebox.showwarning("Respuesta requerida", "Completa todas las preguntas antes de continuar.")
            if tipo == "numero":
                try:
                    numero = float(valor.replace(",", "."))
                    minimo, maximo = datos
                    if not minimo <= numero <= maximo:
                        raise ValueError
                    self.hechos[clave] = int(numero) if numero.is_integer() else numero
                except ValueError:
                    return messagebox.showwarning("Valor inválido", f"Ingresa un número entre {datos[0]} y {datos[1]}.")
            else:
                self.hechos[clave] = valor
        if self.indice_seccion < len(SECCIONES) - 1:
            self.mostrar_seccion(self.indice_seccion + 1)
        else:
            self.mostrar_comentario()

    def mostrar_comentario(self):
        self.limpiar()
        self.estado.configure(text="Contexto adicional · Opcional")
        tarjeta = ctk.CTkFrame(self.contenido, corner_radius=16)
        tarjeta.pack(fill="both", expand=True, padx=70, pady=35)
        ctk.CTkLabel(tarjeta, text="¿Hay algo más que debamos considerar?", font=ctk.CTkFont(size=25, weight="bold")).pack(anchor="w", padx=35, pady=(38, 8))
        ctk.CTkLabel(tarjeta, text="Este comentario aparecerá en tu resumen, pero no modifica automáticamente el diagnóstico.", wraplength=700, justify="left").pack(anchor="w", padx=35)
        self.comentario = ctk.CTkTextbox(tarjeta, height=190)
        self.comentario.pack(fill="x", padx=35, pady=20)
        botones = ctk.CTkFrame(tarjeta, fg_color="transparent")
        botones.pack(fill="x", padx=35, pady=(5, 35))
        ctk.CTkButton(botones, text="← Volver", fg_color="transparent", border_width=1, command=lambda: self.mostrar_seccion(len(SECCIONES)-1)).pack(side="left")
        ctk.CTkButton(botones, text="Ver mi orientación", command=self.mostrar_resultados).pack(side="right")

    def mostrar_resultados(self):
        resultados = evaluar_perfil(self.hechos)
        comentario = self.comentario.get("1.0", "end").strip() if self.comentario else ""
        self.limpiar()
        self.estado.configure(text="Resultado personalizado · Puedes revisar la evidencia de cada hallazgo")
        ctk.CTkLabel(self.contenido, text="Tu orientación académica", font=ctk.CTkFont(size=27, weight="bold")).pack(anchor="w")
        resumen = "No se identificaron alertas prioritarias." if not resultados else f"Se identificaron {len(resultados)} área(s) para priorizar."
        ctk.CTkLabel(self.contenido, text=resumen, text_color=("#526171", "#bac4ce")).pack(anchor="w", pady=(2, 10))
        panel = ctk.CTkScrollableFrame(self.contenido, corner_radius=14)
        panel.pack(fill="both", expand=True)
        for resultado in resultados:
            self._tarjeta_resultado(panel, resultado)
        if not resultados:
            ctk.CTkLabel(panel, text="Mantén tus hábitos actuales y repite la evaluación si tu situación cambia.", font=ctk.CTkFont(size=16)).pack(padx=24, pady=34)
        if comentario:
            ctk.CTkLabel(panel, text="Contexto que compartiste", font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=18, pady=(16, 0))
            ctk.CTkLabel(panel, text=comentario, wraplength=850, justify="left").pack(anchor="w", padx=18, pady=(3, 16))
        ctk.CTkButton(self.contenido, text="Realizar una nueva evaluación", fg_color="transparent", border_width=1, command=self.reiniciar).pack(pady=(12, 0))

    def _tarjeta_resultado(self, panel, resultado):
        colores = {"Alto": "#b33939", "Medio": "#c77d18", "Preventivo": "#2d7a93"}
        tarjeta = ctk.CTkFrame(panel, corner_radius=12)
        tarjeta.pack(fill="x", padx=10, pady=8)
        cabecera = ctk.CTkFrame(tarjeta, fg_color="transparent")
        cabecera.pack(fill="x", padx=18, pady=(15, 3))
        ctk.CTkLabel(cabecera, text=resultado["titulo"], font=ctk.CTkFont(size=18, weight="bold")).pack(side="left")
        ctk.CTkLabel(cabecera, text=resultado["nivel"], fg_color=colores[resultado["nivel"]], corner_radius=8, padx=9, pady=3).pack(side="right")
        ctk.CTkLabel(tarjeta, text=f"{resultado['area']} · {resultado['tipo']}", text_color=("#617080", "#abb6c1")).pack(anchor="w", padx=18)
        ctk.CTkLabel(tarjeta, text=resultado["conclusion"], wraplength=840, justify="left").pack(anchor="w", padx=18, pady=(8, 5))
        ctk.CTkLabel(tarjeta, text="Recomendación: " + resultado["recomendacion"], wraplength=840, justify="left", font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=18, pady=(2, 5))
        if resultado["acciones"]:
            acciones = "Plan de acción:\n" + "\n".join(f"• {accion}" for accion in resultado["acciones"])
            ctk.CTkLabel(tarjeta, text=acciones, wraplength=840, justify="left").pack(anchor="w", padx=18, pady=(3, 6))
        evidencia = ", ".join(resultado["evidencia"])
        ctk.CTkLabel(tarjeta, text=f"Evidencia considerada: {evidencia}", text_color=("#647180", "#9eabb7")).pack(anchor="w", padx=18, pady=(2, 15))

    def reiniciar(self):
        self.hechos, self.respuestas, self.comentario = {}, {}, None
        self.mostrar_bienvenida()


if __name__ == "__main__":
    SistemaExpertoApp().mainloop()
