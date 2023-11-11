#include <iostream>
#include <cmath>

using namespace std;


double f(double m, double v1, double v2, double y)
{
  return sqrt(pow(m, 2) + pow(y, 2)) / v1 + sqrt(pow(1.0 - m, 2) + pow(1 - y, 2)) / v2;
}


double tensearch(double left, double right, double eps, double v1, double v2, double y){ 
    while (right - left > eps){ 
        double m1 = (left * 2 + right) / 3;
        double m2 = (left + right * 2) / 3;
        if (f(m1, v1, v2, y) < f(m2, v1, v2, y))
            right = m2;
        else
            left = m1;
    }
    return (left + right) / 2;
}

int main()
{
  double y, v1, v2;
  cin >> y >> v1 >> v2;
  double res = tensearch(0.0, 1.0, 0.00000001, v1, v2, y);

  printf("%.10f\n", res);

  return 0;
}