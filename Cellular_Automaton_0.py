'''
    Cada linha de saída do programa representa 64 valores booleanos. 
        Verdadeiro = '*'
        Falso = ' '
    A primeira linha é composta de 0's, com o 32º item sendo 1.
    A próxima linha é criada com a seguinte regra:
        O item será verdadeiro se o valor à esquerda ou à direita na linha de cima for 1, não ambos verdadeiros.
        Do contrário, o item será falso.
    
    São exibidas 32 gerações seguindo as regras de construção acima.
'''

#condição inicial
L = 31*[0] + [1] + 32*[0] #estados iniciais
D1 = {1 : '*', 0 : ' '} #if-else de impressão
D2 = {0 : 0, 1 : 1, 2 : 0} #if-else de próxima geração
A = 64*[0]

#número de linhas
for i in range(32):
    #impressão da linha
    for j in range(64): 
        print(D1.get(L[j]), end = '')
    print('')
 
    #próxima geração
    A[0], A[-1] = L[1], L[62]
    for j in range(62):
        A[j+1] = D2.get(L[j]+L[j+2])
    #cópia de A em L
    L = list(A)

'''
Saída:
                               *                                
                              * *                               
                             *   *                              
                            * * * *                             
                           *       *                            
                          * *     * *                           
                         *   *   *   *                          
                        * * * * * * * *                         
                       *               *                        
                      * *             * *                       
                     *   *           *   *                      
                    * * * *         * * * *                     
                   *       *       *       *                    
                  * *     * *     * *     * *                   
                 *   *   *   *   *   *   *   *                  
                * * * * * * * * * * * * * * * *                 
               *                               *                
              * *                             * *               
             *   *                           *   *              
            * * * *                         * * * *             
           *       *                       *       *            
          * *     * *                     * *     * *           
         *   *   *   *                   *   *   *   *          
        * * * * * * * *                 * * * * * * * *         
       *               *               *               *        
      * *             * *             * *             * *       
     *   *           *   *           *   *           *   *      
    * * * *         * * * *         * * * *         * * * *     
   *       *       *       *       *       *       *       *    
  * *     * *     * *     * *     * *     * *     * *     * *   
 *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
'''
