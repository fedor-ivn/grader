from tmpgrader.tests.meme_factory import MemeFactoryTest
from tmpgrader.ibash.ibash import IBash

MemeFactoryTest().test(IBash("solution.sh"))
