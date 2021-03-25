DIR_PUBLICACION="./publicacion"

FCB = "Z.Cookbook.md"
SCB = "Recetario.docx"
S1  = "Tema 1 Introducción, Instalación y primeras pruebas.docx"
S2  = "Tema 2 Primeros ejemplos.docx"
S3  = "Tema 3  Variables tipos y operaciones.docx"
S4  = "Tema 4 Sentencias condicionales y operadores.docx"
S5  = "Tema 5 Bucles e iteraciones.docx"
S6  = "Tema 6 Trabajando con funciones.docx"
S7  = "Tema 7 Colecciones Listas tuplas y diccionarios.docx"
S8  = "Tema 8 Trabajando con ficheros.docx"
S9  = "Tema 9 Clases y Programación Orientada a Objetos.docx"
S10 = "Tema 10 Módulos y librerías.docx"
S11 = "Tema 11 Juegos con pyGame.docx"
S12 = "Tema 12 Servidores y sevicios Web.docx"


all: 0 1 2 3 4 5 6 7 8 9 10 11 12 CB

1:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(S1)  \
					Cabecera.md        \
					Cabecera_latex.md \
					"0.0.0.SobreElCurso.md" \
					"0.1.Introduccion.md" \
					"0.2.ApendiceCompilados_vs_Interpretados.md" \
					"1.1.0.Entornos.md" \
					"1.1.3.Thonny.md" \
					"1.1.8.IntalacionConsola.md" 


2:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(S2)  \
					Cabecera.md        \
					Cabecera_latex.md \
					"2.0.HolaMundo.md" \
					"2.1.UsoConsola.md" \
					"2.2.UsoThonny.md" \
					"2.3.FicherosCodigo.md" \
					"2.4.3.Comentarios.md" \
					"2.4.DepuracionconThonny.md" \
					"2.6.EjecucionLineaComandos.md" \
					"2.8.FixingThonny.md"

3:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(S3)  \
					Cabecera.md        \
					Cabecera_latex.md \
					"3.0.0.Variables.md" \
					"3.0.1.Entrada.md" \
					"3.1.Tipos.md" \
					"3.2.ConversionTipos.md" \
					"3.3.Excepciones.md" \
					"3.4.OperadoresAritmeticos.md" \
					"3.6.cadenas.string.md" 

4:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(S4)  \
					Cabecera.md        \
					Cabecera_latex.md \
					"4.0.SentenciasCondicionales.md" \
					"4.5.3.OperadoresLogicos.md"

5:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(S5)  \
					Cabecera.md        \
					Cabecera_latex.md \
					"5.0.Bucles.md" \
					"5.3.DiferenciasSiVienesDeArduino.md"

6:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					--reference-doc=plantilla.docx \
					-o  $(S6)  \
					Cabecera.md        \
					Cabecera_latex.md \
					6.0.Funciones.md \
					6.1.0.VSCode.md \
					6.1.5.DepuracionFunciones.md \
					6.2.VariablesGlobales.md \
					6.3.FuncionesRecursivas.md \
					6.5.DepuracionVariables.md \
					6.A.CreacionProgramas.md

7:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					--reference-doc=plantilla.docx \
					-o  $(S7)  \
					Cabecera.md        \
					Cabecera_latex.md \
					7.0.TiposColecciones.md \
					7.1.0.Tuplas.md \
					7.1.1.Ejemplo_GeneradorTextos.md \
					7.1.2.Ejemplo_CalculoIRPF.md \
					7.2.0.Listas.md \
					7.2.1.Matrices.md \
					7.2.1.Ejemplo_Juego20Preguntas.md \
					7.3.Diccionarios.md \
					7.4.CadenasYColecciones.md \
					7.4.Ejemplo_Descifrando.md \
					7.6.Conjuntos_Sets.md \
					7.7.Utilidades.md \
					7.8.EjerciosColecciones.md \
					7.9.IndicacionTiposColecciones.md \
					7.A.EjecutandoDsdConsola.md					

8:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					--reference-doc=plantilla.docx \
					-o  $(S8)  \
					Cabecera.md        \
					Cabecera_latex.md \
					8.0.Ficheros.md \
					8.1.0.AdministracionFicheros.md \
					8.1.1.ExploracionRecursivaDirectorios.md \
					8.2.0.LecturaFicheros.md \
					8.2.1.WordCounter.md \
					8.3.0.EscrituraFicheros.md \
					8.3.1.Juego20PreguntasGuardar.md

9:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					--reference-doc=plantilla.docx \
					-o  $(S9)  \
					Cabecera.md        \
					Cabecera_latex.md \
					9.0.ClasesYobjetos.md \
					9.1.ClasesPython.md \
					9.3.0.Herencia.md \
					9.3.1.EjemploSencilloOO.md \
					9.3.2.Juego20Preguntas_OO.md

10:
	pandoc --latex-engine=xelatex \
					--from=markdown \
					-V papersize:a4paper \
					--template=./LaTeX_ES.latex \
					--reference-doc=plantilla.docx \
					-o $(S10) \
					Cabecera.md        \
					Cabecera_latex.md \
					10.0.ModulosLibrerias.md \
					10.1.0.LibreriaEstandar.md \
					10.1.6.Aleatorio.md \
					10.1.7.TrabajandoFechas.md \
					10.3.Instalacionpip.md \
					10.4.BotTelegram.md \
					10.5.0.Jupyter.md \
					10.5.1.RepresentacionDatos.md \
					10.6.Espeak.md


11:
	pandoc --latex-engine=xelatex \
					--from=markdown \
					-V papersize:a4paper \
					--template=./LaTeX_ES.latex \
					--reference-doc=plantilla.docx \
					-o $(S11) \
					Cabecera.md        \
					Cabecera_latex.md \
					11.0.pyGame.md \
					11.0.pyGame.md \
					11.6.Memory.md					

12:
	pandoc --latex-engine=xelatex \
					--from=markdown \
					-V papersize:a4paper \
					--template=./LaTeX_ES.latex \
					--reference-doc=plantilla.docx \
					-o $(S12) \
					Cabecera.md        \
					Cabecera_latex.md \
					12.0.ServidorWeb.md \
					12.1.ServidorWeb_flask.md \
					12.2.Ejemplo_Calculo_irpf.md \
					12.5.1.ServiciosWeb.md   

CB:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(SCB)  \
					Cabecera.md        \
					Cabecera_latex.md \
					$(FCB)


10.0.ModulosLibrerias.md
10.1.0.LibreriaEstandar.md
10.1.1.sys.md
10.1.2.math.md
10.1.4.zip.md
10.1.6.Aleatorio.md
10.1.7.TrabajandoFechas.md
10.3.Instalacionpip.md
10.4.BotTelegram.md
10.5.0.Jupyter.md
10.5.1.RepresentacionDatos.md
10.5.2.Jupy_ProbabilidadCumpleaños_v2.md
10.5.2.Pandas_v2.md
10.5.Comparativa_tiempos_v2.md
10.5.Cumpleaños_v2.ipynb
10.5.numpy_v2.md
10.6.Espeak.md
10.7.SpechToText_v2.md
10.8.pdf_v2.md
