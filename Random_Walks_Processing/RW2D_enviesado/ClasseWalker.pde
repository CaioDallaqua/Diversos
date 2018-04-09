class Walker{
  int x, y;
  Walker(){
    //método construtor
    //inicializa o walker no centro
    x = width/2;
    y = height/2;
  }
  void display(){
    stroke(0);
    point(x,y);
  }
  void step(){
    //realiza o passo do walker
    //a função random retorna um float f, tal que 0 <= f < 3
    //ao converter pra int, como int arredonda pra baixo,
    //os retornos possíveis são 0, 1, 2
    //por isso subtraímos 1, assim ficamos com -1, 0, 1 (pra um lado, fica no mesmo lugar, pro outro)
    int passo = random(100);
    if(passo <= 10) x++; //10% pra direita
    else if(passo <= 50) x--; //40% pra esquerda
    else if(passo <= 70) y++; //20% pra cima
    else y--; //30% pra baixo
    
    //mantém o walker na tela
    x = constrain(x, 0, width-1);
    y = constrain(y, 0, height-1);
  }
}
