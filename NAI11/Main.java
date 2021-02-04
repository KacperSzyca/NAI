package com.company;

public class Main {
    public static void main(String[] args) {
        int[] inputs = {3,5,2};
        int[] weights = {4,3,1};
        Neuron neuron = new Neuron(inputs,weights,2);
        System.out.println(neuron.output());
    }
}
