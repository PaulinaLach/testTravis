#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MAIN
#define BOOST_TEST_MODULE MyTest
#include <boost/test/unit_test.hpp>
#include <lib.hpp>

BOOST_AUTO_TEST_CASE( test2 )
{
    BOOST_CHECK( method2() == 3 );        // SUCCESS
    BOOST_REQUIRE( defaultMethod() == 0 );      // SUCCESS
}
