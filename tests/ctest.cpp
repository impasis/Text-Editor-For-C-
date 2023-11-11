#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> v = {1, 0, 2, 3};

	for (auto& el : v)
		cout << el << " ";

	return 0;
}