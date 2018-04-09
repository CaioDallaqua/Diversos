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
    int passox = int(random(3))-1;
    int passoy = int(random(3))-1;
    x += passox;
    y += passoy;
    //mantém o walker na tela
    x = constrain(x, 0, width-1);
    y = constrain(y, 0, height-1);
  }
}
