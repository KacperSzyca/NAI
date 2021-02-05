package pl.pjatk;

import guru.nidi.graphviz.engine.Graphviz;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.net.URL;
import java.util.*;
//https://java2blog.com/dijkstra-java/
import static guru.nidi.graphviz.engine.Format.PNG;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Podaj nazwe pliku .txt");
        String file = scan.nextLine();
        System.out.println("Podaj wierzchołek startowy");
        String firstVertex = scan.nextLine();
        System.out.println("Podaj wierzchołek końcowy");
        String lastVertex = scan.nextLine();
        List<Vertex> vertexList = new ArrayList<>();
        Set<String> vertexNamesList = new HashSet<>();
        String lastResult = "";
        try {
            BufferedReader reader = new BufferedReader(new FileReader("src/main/resources/" + file));

            vertexNamesList.add(firstVertex);
            // przeczykac plik
            String line;
            while (true) {
                line = reader.readLine();
                if (line == null)
                    break;
                String vertexName = line.substring(line.indexOf("$") + 1, line.indexOf("!"));
                vertexNamesList.add(vertexName);
            }
            for (String name : vertexNamesList) {
                vertexList.add(new Vertex(name));
            }
            BufferedReader reader2 = new BufferedReader(new FileReader("src/main/resources/" + file));
            String line2;
            List<String> dataList = new ArrayList<>();
            while (true) {
                String data = "";
                line2 = reader2.readLine();
                if (line2 == null)
                    break;
                data += line2.substring(line2.indexOf("$") + 1, line2.indexOf("!")) + " ";
                data += line2.substring(line2.indexOf("&") + 1, line2.indexOf("#")) + " ";
                data += line2.substring(line2.indexOf(":") + 1, line2.indexOf("}"));
                dataList.add(data);
            }

            for (String vertexDetails : dataList) {
                int index = Integer.parseInt(vertexDetails.split(" ")[0]) - 1;
                int destination = Integer.parseInt(vertexDetails.split(" ")[1]) - 1;
                int val = Integer.parseInt(vertexDetails.split(" ")[2]);
                if(index != destination && val > 0) {
                vertexList.get(index).addNeighbour(new Edge(val, vertexList.get(index), vertexList.get(destination)));
                }
            }
            for (String as : dataList)
            {
                String index = as.split(" ")[0];
                String desc = as.split(" ")[1];
                int val = Integer.parseInt(as.split(" ")[2]);
                if(index != desc && val > 0) {
                    lastResult += "\n" + index + " -> " + desc + ";";
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        DijkstraShortestPath shortestPath = new DijkstraShortestPath();
        int vertexIndex = Integer.parseInt(firstVertex)-1;
        shortestPath.computeShortestPaths(vertexList.get(vertexIndex));
        System.out.println("Shortest Path from A to E: " + shortestPath.getShortestPathTo(getVertexByName(lastVertex, vertexList)));
        List<Vertex> bestRoute = shortestPath.getShortestPathTo(getVertexByName(lastVertex, vertexList));
        String bestRouteData = "";
        for(Vertex x: bestRoute){
            bestRouteData += x.getName() + " ";
        }
        bestRouteData += ";";
        String src = "digraph G { \nnode [shape = doublecircle]; " + bestRouteData + "\n  node [shape = circle]; " + lastResult + "\n}";

        try{
            Graphviz.fromString(src).render(PNG).toFile(new File("test.png"));
        }catch (Exception e){
            e.printStackTrace();
        }
        String routeData ="";

        for (Vertex v: vertexList){
                routeData += v.getName() + " -> ";
                if(vertexList.size()%1 == 0){
                    routeData += ";";
                }
        }
    }

//    digraph G {
//        node [shape = doublecircle]; l1 l2;
//        node [shape = circle];
//        l1 -> l2;
//        l1 -> l3;
//    }


    public static Vertex getVertexByName(String name, List<Vertex> vertexList) {
        for (Vertex v : vertexList) {
            if (v.getName().equals(name)) {
                return v;
            }
        }
        return null;
    }
}
