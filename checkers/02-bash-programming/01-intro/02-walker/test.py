from tmpgrader.tests.walker import WalkerTest
from tmpgrader.ibash.ibash import IBash

WalkerTest().test(IBash("reference-solution.sh"))
