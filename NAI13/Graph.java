package pl.pjatk;

import guru.nidi.graphviz.engine.Format;
import guru.nidi.graphviz.engine.Graphviz;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.RenderedImage;
import java.io.File;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import static guru.nidi.graphviz.engine.Format.PNG;

public class Graph {
    private List<GraphRow> graphRows = new ArrayList<>();

    public Graph() {
    }

    public void addEdge(int start,int end, int iterator){
        graphRows.add(new GraphRow(start,end,iterator));
    }

    public void print() {
       // graphRows.sort(Comparator.comparing(GraphRow::getNumer));
        String src = "digraph G { \n ";
        for (int i = 0; i < graphRows.size(); i++) {
                    src += "\"" + graphRows.get(i).getX()  + "\" -> \"" + graphRows.get(i).getY()  + "\" \n";

        }
        src+= " }";

        try{
            Graphviz.fromString(src).render(PNG).toFile(new File("test.png"));
        }catch (Exception e){
            e.printStackTrace();
        }
    }



}
