package com.company;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int[] inputsN1 = {1, 3};
        int[] weightsN1 = {1, 2};
        int[] inputsN2 = {2, 1};
        int[] weightsN2 = {1, 2};
        int[] inputsN3 = {3, 2};
        int[] weightsN3 = {2, 1};
        Neuron N1 = new Neuron(inputsN1, weightsN1, 1);
        Neuron N2 = new Neuron(inputsN2, weightsN2, 0);
        List<Neuron> neuronList = new ArrayList<>();
        neuronList.add(N1);
        neuronList.add(N2);
        Neuron N3 = new Neuron(inputsN3, weightsN3, 1, neuronList);
        System.out.println(N3.showNeuronParameters());
    }
}
