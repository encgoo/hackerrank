#include <iostream>
using namespace std;
enum class Fruit { apple, orange, pear };
enum class Color { red, green, orange };

template <typename T> struct Traits;

// Define specializations for the Traits class template here.
#include <string>
string get_name(Fruit f)
{
    static string names[] = {"apple", "orange", "pear"};
    return names[(int) f];
}

string get_name(Color c)
{
    static string names[] = {"red", "green", "orange"};
    return names[(int) c];
}
template<typename T> 
class Traits
{
public:
    static string name(int index)
    {
        if (index > 2 || index < 0)
        {
            return "unknown";
        }
        T input = (T) index;
        return get_name(input);
    }
};

