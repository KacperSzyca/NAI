package pl.pjatk;

import guru.nidi.graphviz.engine.Format;
import guru.nidi.graphviz.engine.Graphviz;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.RenderedImage;
import java.io.File;

import static guru.nidi.graphviz.engine.Format.PNG;

public class Graph {
    private final Integer[][] pos;
    private final int wierzcholki;

    public Graph(int wierzcholki) {
        this.wierzcholki = wierzcholki;
        this.pos = new Integer[wierzcholki][wierzcholki];
    }

    public void addEdge(int start,int end){
        pos[start][end] = 1;
    }

    public void print() {
        String src = "digraph prof { ";
        for (int i = 0; i < wierzcholki; i++) {
            for (int j = 0; j < wierzcholki; j++) {
                if (pos[i][j] != null) {
                    src += "\"" + i  + "\" -> \"" + j + "\" ";
                }
            }
        }
        src+= " }";
        try{
            Graphviz.fromString(src).render(PNG).toFile(new File("C:\\Users\\user\\Desktop\\NAI13-Grafy\\test.png"));
        }catch (Exception e){
            e.printStackTrace();
        }
    }



}
