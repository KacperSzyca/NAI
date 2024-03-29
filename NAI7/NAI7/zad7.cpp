#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <random>
#include <cmath>
#include <numeric>
#include <algorithm>

using namespace std;
random_device r;
default_random_engine e1(r());


//minimalizacja
auto hill_climbing_r_alg = [](auto get_random_sol, auto get_all_neighbours, auto goal, int max_iterations) {
    auto current_solution = get_random_sol();
    for (int iteration = 0; iteration < max_iterations; iteration++)
    {
        auto next_solutions = get_all_neighbours(current_solution);
        uniform_int_distribution<int> uniform_dist(0, next_solutions.size() - 1);
        auto next_sol = next_solutions.at(uniform_dist(e1));
        if (goal(current_solution) > goal(next_sol)) {
            current_solution = next_sol;
        }
    }
    return current_solution;
};

int main(int argc, char* argv[])
{
    if (argc  < 4 || argc > 5)
    {
        cout << "B��dnie podana ilo�� argument�w";
        return -1;
    }
    int function_choice = stoi(argv[1]);
    int max_iterations = stoi(argv[2]);
    int x = stoi(argv[3]);
    int y = stoi(argv[4]);

    uniform_real_distribution<double> uniform_dist( x, y);



    auto booth = [](vector<double> d) {
        double x = d.at(0);
        double y = d.at(1);
        return pow(x + 2 * y - 7, 2) + pow(2 * x + y - 5, 2);
    };

    auto himmelblau = [](vector<double> d) {
        double x = d.at(0);
        double y = d.at(1);
        return pow(x * x + y - 11, 2.0) + pow(x + y * y - 7, 2);
    };

    auto matyas = [](vector<double> d) {
        double x = d.at(0);
        double y = d.at(1);
        return  (0.26 * (x * x + y * y)) - (0.48 * x * y);
    };

   
    auto goal =  function_choice == 1 ? booth : function_choice == 2 ? himmelblau : matyas;
   

    auto neighbours = [](vector<double> x, double dx = 0.001) {
        vector<vector<double>> ret;
        for (int i = 0; i < x.size(); i++)
        {
            auto nx = x;
            nx[i] += dx;
            ret.push_back(nx);
            nx[i] -= 2.0 * dx;
            ret.push_back(nx);
        }
        return ret;
    };

    auto init = [&uniform_dist]() {
        vector<double> x(2);
        x[0] = uniform_dist(e1);
        x[1] = uniform_dist(e1);
        return x;
    };

   
    auto solution = hill_climbing_r_alg(
        //    auto solution = hill_climbing_alg(
        init,
        neighbours,
        goal,
        max_iterations);

    cout << "result: [ ";
    for (auto e : solution)
        cout << e << " ";
    cout << "] -> " << goal(solution) << endl;
}