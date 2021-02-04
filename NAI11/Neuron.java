package com.company;

public class Neuron implements NeuronInterface{
    private int[] inputs;
    private int[] weights;
    private int bias;

    public Neuron(int[] inputs, int[] weights, int bias) {
        this.inputs = inputs;
        this.weights = weights;
        this.bias = bias;
    }

    public double output(){
        double sum =0.00;
        for(int i=0;i<this.inputs.length;i++){
            sum+= this.weights[i] * this.inputs[i];
        }
        return activate(sum+this.bias);
    }

    @Override
    public Double activate(Double value){
        return 1 / (1 + Math.pow(Math.E,-value));
    }
}
