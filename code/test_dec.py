import logging
import test_wrap


@test_wrap.timeCountWrapper
@test_wrap.setupConfigsWrapper
@test_wrap.loopAntennaWrapper
@test_wrap.loopPowerWrapper
@test_wrap.loopChannelWrapper
def method_run(olog):
    # olog.info('Inputs: {}'.format(None))
    pass


logging.basicConfig(level=logging.INFO)
logging.info('Start~')
res = method_run(logging)
print(len(res))
print(res)
