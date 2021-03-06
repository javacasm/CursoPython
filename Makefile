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

1bis:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					--reference-doc=plantilla.docx \
					-o  'prueba_'$(S1)  \
					Cabecera.md        \
					Cabecera_latex.md \
					"0.0.0.SobreElCurso.md" \
					"0.1.Introduccion.md" \
					"0.2.ApendiceCompilados_vs_Interpretados.md" \
					"1.1.0.Entornos.md" \
					"1.1.3.Thonny.md" \
					"1.1.8.IntalacionConsola.md" 

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
					-o  $(S6)  \
					Cabecera.md        \
					Cabecera_latex.md \
					6.0.Funciones.md \
					6.1.0.VSCode.md \
					6.1.5.DepuracionFunciones.md \
					6.2.VariablesGlobales.md \
					6.3.FuncionesRecursivas.md \
					6.5.DepuracionVariables.md

CB:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(SCB)  \
					Cabecera.md        \
					Cabecera_latex.md \
					$(FCB)

12:
	pandoc --latex-engine=xelatex \
					--from=markdown \
					-V papersize:a4paper \
					--template=./LaTeX_ES.latex \
					-o $(S12) \
					Cabecera.md        \
					Cabecera_latex.md \
					12.0.ServidorWeb.md \
					12.1.ServidorWeb_flask.md \
					12.2.Ejemplo_Calculo_irpf.md \
					12.5.1.ServiciosWeb.md   

11:
	pandoc --latex-engine=xelatex \
					--from=markdown \
					-V papersize:a4paper \
					--template=./LaTeX_ES.latex \
					-o $(S11) \
					Cabecera.md        \
					Cabecera_latex.md \
					"11.0.pyGame.md" 


clean:
	rm $(S5) $(S6) $(S1) $(S2) $(S3) $(S4) $(SFAQ)

publish:
	cp $(s7) $(S5) $(S6) $(S1) $(S2) $(S3) $(S4) $(SFAQ) $(SMAT) $(DIR_PUBLICACION)
	cp *Objetivos*.pdf $(DIR_PUBLICACION)
	cp *Ejercicio*.pdf $(DIR_PUBLICACION)
	cp *Test*.pdf $(DIR_PUBLICACION)


push:
	git commit -m "update" $(S7);
	git commit -m "update" $(S5);
	git commit -m "update" $(S6);
	git commit -m "update" $(S3);
	git commit -m "update" $(S4);
	git commit -m "update" $(S2);
	git commit -m "update" $(S1);
	git push;

