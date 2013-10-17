#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MAIN
#define BOOST_TEST_MODULE MyTest
#include <boost/test/unit_test.hpp>
#include <lib.hpp>

BOOST_AUTO_TEST_CASE( test1 )
{
    BOOST_CHECK( method1(1) == 1 );        // SUCCESS

    BOOST_REQUIRE( method1(2) == 2 );      // FAIL
}
