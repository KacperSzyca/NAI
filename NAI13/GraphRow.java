package pl.pjatk;

public class GraphRow {
    private int x;
    private int y;
    private int numer;

    public GraphRow(int x, int y, int numer) {
        this.x = x;
        this.y = y;
        this.numer = numer;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getNumer() {
        return numer;
    }

    public void setNumer(int numer) {
        this.numer = numer;
    }
}
