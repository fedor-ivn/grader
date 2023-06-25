from tmp_grader.tests.meme_factory import MemeFactoryTest
from tmp_grader.ibash.ibash import IBash

MemeFactoryTest().test(IBash("solution.sh"))
