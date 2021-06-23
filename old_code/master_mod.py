#module is executed once in a program
print "not in module"
import module01
module01.func_test(20)
module01.func_test(200)
print module01.__name__
import module01 #not executed 
print "reloading module"
reload(module01)
import module02
module02.marker(5)
import package_test
package_test.god()
package_test.demon()