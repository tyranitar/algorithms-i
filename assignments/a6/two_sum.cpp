#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>

// TODO: WIP, could never get the input to read correctly.
int main() {
    std::ifstream infile("data/algo1-programming_prob-2sum.txt");

    if (!infile.is_open()) {
        return 0;
    }

    std::vector<int> A(1000000, 0);
    std::vector<int> T(20001, 0);
    std::set<int> S;

    int x;
    int idx = 0;
    std::string s;

    while (getline(infile, s)) {
        A[idx] = std::stoi(s);
        idx++;
    }

    std::cout << idx << std::endl;

    infile.close();

    int A_size = A.size();

    for (int t = -10000; t < 10001; t++) {
        for (int j = 0; j < A_size; j++) {
            x = A[j];

            if ((S.find(t - x) != S.end()) && (x != t - x)) {
                T[t + 10000] = 1;
            }
        }

        // std::cout << t << std::endl;
    }

    int count = 0;

    for (int t = 0; t < 20001; t++) {
        if (T[t] == 1) {
            count++;
        }
    }

    std::cout << "count: " << count;

    return 0;
}