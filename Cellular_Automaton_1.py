'''
    Cada linha de saída do programa representa 31 valores booleanos.
    A primeira linha é composta por 0's, com o 16º item sendo 1.
    Regras:
            (1,1,1) = 0
            (1,1,0) = 0
            (1,0,1) = 0
            (1,0,0) = 1
            (0,1,1) = 1
            (0,1,0) = 1
            (0,0,1) = 1
            (0,0,0) = 0
            
    São exibidas 16 gerações seguindo as regras de construção acima.
'''

#lista na condição inicial
L = 15*[0] + [1] + 15*[0] #estados iniciais
D1 = {0 : ' ', 1 : '*'} #if-else impressão
D2 = {0 : 0, 1 : 1, 2 : 0} #if-else bordas
A = 31*[0]

#número de linhas
for i in range(16):
    
    #impressão da linha
    for j in range(31):
        print(D1.get(L[j]), end = '')
    print('')
    
    #próxima geração
    A[0] = D2.get(L[0]+L[1])
    for j in range(29):
        if L[j]+L[j+1]+L[j+2] == 1:
            A[j+1] = 1
        elif not L[j] and L[j+1]+L[j+2] == 2:
            A[j+1] = 1
        else:
            A[j+1] = 0
    A[-1] = D2.get(L[-1]+L[-2])
    #cópia de A em L
    L = list(A)
    
'''
Saída:
               *               
              ***              
             **  *             
            ** ****            
           **  *   *           
          ** **** ***          
         **  *    *  *         
        ** ****  ******        
       **  *   ***     *       
      ** **** **  *   ***      
     **  *    * **** **  *     
    ** ****  ** *    * ****    
   **  *   ***  **  ** *   *   
  ** **** **  *** ***  ** ***  
 **  *    * ***   *  ***  *  * 
** ****  ** *  * *****  *******
'''
