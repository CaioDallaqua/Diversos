Walker w;

void setup(){
  size(400, 400);
  //cria um objeto walker
  w = new Walker();
  //seta a cor do fundo
  background(255);
}

void draw(){
  //move o walker e o mostra na tela
  w.step();
  w.display();
}
