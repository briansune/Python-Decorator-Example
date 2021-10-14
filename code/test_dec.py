import timeit
import logging
from time import sleep


def timerWrapper(oFunction):
    def funcWrapper(*args, **kwargs):
        f_start_time = timeit.default_timer()
        a_func_res = oFunction(*args, **kwargs)
        f_stop_time = timeit.default_timer()
        o_log = None
        for arg in args:
            if 'logging' in str(arg):
                o_log = arg
                break
        if o_log:
            o_log.info('Total run time: {:.3f}'.format(f_stop_time - f_start_time))
        return a_func_res
    return funcWrapper


@timerWrapper
def method_run(a, b, olog):
    olog.info('Inputs: {}'.format([a, b]))
    sleep(1)
    return a + b


logging.basicConfig(level=logging.INFO)
logging.info('Start~')
res = method_run(1, 2, logging)
logging.info('Result: {}'.format(res))
