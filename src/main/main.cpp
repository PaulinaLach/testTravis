#include <iostream>
#include <boost/program_options.hpp>
#include <lib.hpp>

namespace po = boost::program_options;

int main(int ac, char** av){
    // Declare the supported options.
    po::options_description desc("Allowed options");
    desc.add_options()
    ("help", "produce help message")
    ("method", po::value<int>(), "set compression level");

    po::variables_map vm;
    po::store(po::parse_command_line(ac, av, desc), vm);
    po::notify(vm);    

    if (vm.count("help")) {
        std::cout << desc << "\n";
        return 1;
    }

    if (vm.count("method")) {
        std::cout << "method to call " 
        << vm["method"].as<int>() << ".\n";
        switch (vm["method"].as<int>())
        {
            case 1:
                method1(1);
                break;
            case 2:
                method2();
                break;
            default:
                defaultMethod();
                break;
        }
    } else {
        std::cout << "no given method to call. Calling default method\n";
        defaultMethod();
    }
}
