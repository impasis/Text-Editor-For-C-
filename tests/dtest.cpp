#include <iostream>

using namespace std;

struct student
{
	double n;
	string name;
};


int main()
{
	int n;
	cin >> n;
	student arr[n];

	for (int i = 0; i < n; i++){
		int a, b, c;
		string name;
		cin >> name >> a >> b >> c;
		double d = double(a + b + c) / 3;

		arr[i].n = d;
		arr[i].name = name;
	}


	for (int i = 0; i < n; i++)
		cout << arr[i].name << " " << arr[i].n << endl;

	return 0;
}
