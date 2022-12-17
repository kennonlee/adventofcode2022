import sys

class Sensor:
    def calc_mdist(pta, ptb):
        return sum(map(lambda a,b: abs(a-b), pta, ptb))
    
    def __init__(self, loc, beacon):
        self.loc = loc
        self.beacon = beacon
        self.mdist = Sensor.calc_mdist(loc, beacon)

    def get_coverage(self, y):
        ret = set()
        dist = Sensor.calc_mdist(self.loc, (self.loc[0], y)) 
        if dist > self.mdist:
            return ret
        for i in range (self.mdist - dist + 1):
            ret.add(self.loc[0] + i)
            ret.add(self.loc[0] - i)
#        print(vars(self), ret)
        return ret

def parse_sensors(lines):
    sensors = []
    for line in lines:
        tokens = line.split()
        locx = int(tokens[2].split('=')[1][:-1])
        locy = int(tokens[3].split('=')[1][:-1])
        beaconx = int(tokens[-2].split('=')[1][:-1])
        beacony = int(tokens[-1].split('=')[1])
        sensors.append(Sensor((locx, locy), (beaconx, beacony)))
    return sensors

def get_line_coverage(sensors, y):
    coverage = set()
    for s in sensors:
        coverage.update(s.get_coverage(y))
    for s in sensors:
        if s.beacon[1] == y and s.beacon[0] in coverage:
            print('removing beacon at', s.beacon)
            coverage.remove(s.beacon[0])
    return coverage

def print_coverage(sensors, x1, y1, x2, y2, coverage, y):
    for j in range(y1, y2):
        for i in range(x1, x2):
            pass

sensors = parse_sensors(sys.stdin.readlines())
#for s in sensors:
#    print(vars(s))

y = 2000000
#y = 10
coverage = get_line_coverage(sensors, y)
#print(coverage)
print(len(coverage))

