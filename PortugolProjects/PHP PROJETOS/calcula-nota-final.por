programa
{
	inclua biblioteca Internet
	inclua biblioteca Tipos
	funcao inicio()
	{
		real nota1,nota2,nota3,nota4,nota5,nota6,nota7
		cadeia aluno 
		real notaMaxima,somaDasNotasDoAluno,notaFinalDoAluno
		notaMaxima = 70
		
		escreva(" Nome inteiro do Aluno: ")
		leia(aluno)
		escreva ("\n")

		nota1 = digitarNota("nota 1")
		escreva ("\n")
		
		nota2 = digitarNota("nota 2")
		escreva ("\n")
		
		nota3 = digitarNota("nota 3")
		escreva ("\n")
		
		nota4 = digitarNota("nota 4")
		escreva ("\n")
		
		nota5 = digitarNota("nota 5")
		escreva ("\n")
		
		nota6 = digitarNota("nota 6")
		escreva ("\n")
		
		nota7 = digitarNota("nota 7")
		escreva ("\n\n\n\n")
		
          somaDasNotasDoAluno = (nota1+nota2+nota3+nota4+nota5+nota6+nota7)
          escreva (" Total das notas do aluno: " + somaDasNotasDoAluno)
          escreva ("\n\n")
          
		notaFinalDoAluno = somaDasNotasDoAluno*100/notaMaxima 
		
		escreva(" Nome do Aluno: " + aluno)
		escreva ("\n\n")
		
		escreva(" O aluno atingiu: " + notaFinalDoAluno + "%")
		escreva ("\n\n")
		se(notaFinalDoAluno>=70) {
	        escreva (" Por isso foi aprovado! ")
		}
		senao{   
		  escreva (" Infelizmente por isso foi reprovado! ")
		}
		escreva ("\n")
		
	}
	funcao real digitarNota(cadeia nomeNota){
		real nota
		cadeia notaTemp
		logico saia
		saia = falso
		nota = 0
		faca { 
			escreva(" Digite a " + nomeNota + " do Aluno: ")
		     leia(notaTemp)
		     
               se (validarNotaDigitada(notaTemp)) {
               	saia = verdadeiro
               	nota = Tipos.cadeia_para_real(notaTemp)
               } senao {
	     	   escreva (" Digite uma nota entre 0 a 10")
	     	   escreva ("\n\n")
               }
		}enquanto (saia == falso)
		
		retorne nota
	} 
	funcao logico validarNotaDigitada(cadeia nota) {
		real notaTemp
		
	     se (verificarSeNotaEstaNoIntervalo(nota)) {
	         	 retorne verdadeiro
	     }
	     retorne falso
	}
		
	funcao logico verificarSeNotaEstaNoIntervalo(cadeia nota) {
		real notaTemp
		se (verificarSeDigitouNumero(nota)){
			notaTemp = Tipos.cadeia_para_real(nota)
		    se (notaTemp >= 0 e notaTemp <= 10) {
	         	  retorne verdadeiro
	         }
		}
	     retorne falso
	}
	funcao logico verificarSeDigitouNumero(cadeia nota) {
		se (Tipos.cadeia_e_real(nota) ou Tipos.cadeia_e_inteiro(nota, 10)) { 
			retorne verdadeiro
	     }
	     retorne falso
	}

}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2106; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */