package com.company;

import java.util.Arrays;
import java.util.List;

public class Neuron implements NeuronInterface {
    private int[] inputs;
    private int[] weights;
    private int bias;
    private List<Neuron> childList;

    public Neuron(int[] inputs, int[] weights, int bias) {
        this.inputs = inputs;
        this.weights = weights;
        this.bias = bias;
    }

    public Neuron(int[] inputs, int[] weights, int bias, List<Neuron> childList) {
        this.inputs = inputs;
        this.weights = weights;
        this.bias = bias;
        this.childList = childList;
    }

    public double weightedSumOfInputs() {
        double sum = 0.0;
        double weightedSum = 0.0;
        for (int i = 0; i < this.weights.length; i++) {
            sum += this.weights[i] * this.inputs[i];
            weightedSum += this.weights[i];
        }
        return sum / weightedSum;
    }

    public double sum() {
        double sum = 0.0;
        for (int i = 0; i < this.inputs.length; i++) {
            sum += this.weights[i] * this.inputs[i];
        }
        return sum + this.bias;
    }

    public double output() {
        return activate(sum());
    }

    public String showNeuronParameters() {
        String neuronParameters = "-------------\n" +
                "Neuron inputs: " + Arrays.toString(this.inputs) + "\n" +
                "Neuron weights: " + Arrays.toString(this.weights) + "\n" +
                "Neuron bias: " + bias + "\n" +
                "Neuron weighted sum of inputs: " + weightedSumOfInputs() + "\n" +
                "Neuron output: " + output() + "\n";
        if (this.childList != null) {
            neuronParameters += showChilds();
        }
        return neuronParameters;

    }

    public String showChilds() {
        String show = "";
        if (childList.size() == 1) {
            show += "\n---Neuron child: ---\n" + childList.get(0).showNeuronParameters();
        } else {
            show += "\n---Neuron childs: ---\n";
            for (Neuron child : childList) {
                show += child.showNeuronParameters();
            }
        }
        return show;
    }

    @Override
    public Double activate(Double value) {
        return 1 / (1 + Math.pow(Math.E, -value));
    }
}
