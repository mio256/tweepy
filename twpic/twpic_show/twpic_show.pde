import processing.net.*;
PImage img;

int port = 10001; // 適当なポート番号を設定

Server server;

void setup() {
  size(250, 250);
  server = new Server(this, port);
  // IPアドレスを出力
  //println("server address: " + server.ip()); 
  //set foreground
  surface.setAlwaysOnTop(true);
  //resize
  surface.setResizable( true );
}

void draw() {
  Client client = server.available();
  if (client !=null) {
    try {
      String whatClientSaid = client.readString();
      if (whatClientSaid != null) {
        // Pythonからのメッセージを出力
        //println(whatClientSaid); 
        String dst_path=whatClientSaid;
        //fill(0);
        //text(whatClientSaid, x_pos, y_pos);
        //y_pos+=20;
        img = loadImage(dst_path);
        img.resize(0, height);
        background(255);
        image(img, 0, 0);
      }
    }
    catch(ArrayIndexOutOfBoundsException e){
      
    }
  }
}
