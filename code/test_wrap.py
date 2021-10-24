import timeit
import logging
from numpy import array

# global variables
l_cfgs_antenna = [[0, 1], [0], [1]]
l_cfgs_channel = [[11, 12, 13], [25, 26]]
l_cfgs_power = [[0, 1, 2], [7], [3, 4, 5]]

l_antenna = []
l_channel = []
l_power = []


def timeCountWrapper(oFunction):
    def funcWrapper(*args, **kwargs):
        f_start_time = timeit.default_timer()
        l_res = oFunction(*args, **kwargs)
        f_stop_time = timeit.default_timer()
        logging.info('Total run time: {:.3f}'.format(f_stop_time - f_start_time))
        return l_res

    return funcWrapper


def setupConfigsWrapper(oFunction):
    def funcWrapper(*args, **kwargs):
        global l_cfgs_antenna
        global l_cfgs_power
        global l_cfgs_channel

        global l_antenna
        global l_power
        global l_channel

        l_res = []

        i_len = min(len(l_cfgs_antenna), len(l_cfgs_power), len(l_cfgs_channel))
        for i in range(i_len):
            l_antenna = l_cfgs_antenna[i]
            l_power = l_cfgs_power[i]
            l_channel = l_cfgs_channel[i]

            logging.info(l_antenna)
            logging.info(l_power)
            logging.info(l_channel)
            l_res.append(array(oFunction(*args, **kwargs)).flatten().tolist())
        return l_res

    return funcWrapper


def loopAntennaWrapper(oFunction):
    def funcWrapper(*args, **kwargs):
        global l_antenna
        l_res_tmp = []
        for i in l_antenna:
            logging.info('run ANT# {}'.format(i))
            l_res_tmp += [oFunction(*args, **kwargs)]
        return l_res_tmp

    return funcWrapper


def loopPowerWrapper(oFunction):
    def funcWrapper2(*args, **kwargs):
        global l_power
        l_res_tmp = []
        for i in l_power:
            logging.info('run PWR# {}'.format(i))
            l_res_tmp += [oFunction(*args, **kwargs)]
        return l_res_tmp

    return funcWrapper2


def loopChannelWrapper(oFunction):
    def funcWrapper3(*args, **kwargs):
        global l_channel
        l_res_tmp = []
        for i in l_channel:
            logging.info('run CH# {}'.format(i))
            l_res_tmp += [oFunction(*args, **kwargs)]
        return l_res_tmp

    return funcWrapper3
