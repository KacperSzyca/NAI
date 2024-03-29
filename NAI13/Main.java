package pl.pjatk;

import guru.nidi.graphviz.engine.Graphviz;
import guru.nidi.graphviz.engine.GraphvizServerEngine;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws Exception {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("C:\\Users\\user\\PycharmProjects\\NAI\\java\\NAI13-Grafy\\dane.txt"));


            Graph graph = new Graph();
            String line;
            for(int i=0; 1==1;i++){
                line = reader.readLine();
                if(line==null)
                    break;
                addEdge(graph,line, i);
            }
            reader.close();

            graph.print();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void addEdge(Graph graph,String line, int number){
        int start = Integer.parseInt(line.substring(line.indexOf("$") + 1, line.indexOf("!")));
        int end = Integer.parseInt(line.substring(line.indexOf("&") + 1, line.indexOf("#")));
        graph.addEdge(start,end, number);
    }
}