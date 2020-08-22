An example file structure

```text
Courses\
	Optimisation\
		preamble.tex
		lec1.tex
		lec2.tex
		...
		lec12.tex
	VP\
		preamble.tex
		lec1.tex
		lec2.tex
		...
		lec12.tex
		
> Courses> python3 run.py Optimisation\


Courses\
	Optimisation.tex
	Optimisation\
		preamble.tex
		lec1.tex
		lec2.tex
		...
		lec12.tex
	VP\
		preamble.tex
		lec1.tex
		lec2.tex
		...
		lec12.tex
		
```
Each LecX.tex should compile on it's own, and Optimisation should compile on it's own

A more in depth example:

```text
\Courses
	Optimisation\
		preamble.tex
		lec1.tex
		lec2.tex
		lec3.tex
		figures\
			fig1.png
			fig2.jpg
			
> Courses> python3 Lect_Stack.py Optimisation\

\Courses
	Optimisation.tex
	\Optimisation
		...
```

		
		
		
		
		
		
		
		
		
		