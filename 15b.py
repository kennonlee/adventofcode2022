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
        return ret

    #   01234567
    #0 o..........
    #1 .o......... 0,1
    #2 ..o........
    #3 ...o.......
    #4 ....o......
    #5 .....o.....
    #6 o...o#o.... 
    #7 .o.o###o... 
    #8 ..o#####o.. 4,8 mdist 2
    #9 .o.o###o.o.
    #0 o...o#o...o
    #1 .....o.....    
    #2 ....o......    
    #3 ...o.......    
    #4 ..o........    
    #5 .o.........    
    #6 o..........    
    
    # return lines that bound the sensor one beyond its mdist 
    # the distress beacon should be at the intersection of these
    def get_bounds(self):
        ret = set()
        left = (self.loc[0] - self.mdist - 1, self.loc[1])
        right = (self.loc[0] + self.mdist + 1, self.loc[1])
        top = (self.loc[0], self.loc[1] - self.mdist - 1)
        bottom = (self.loc[0], self.loc[1] + self.mdist + 1)        

        ret.add((1, left[1] - left[0]))
        ret.add((-1, left[1] + left[0]))
        ret.add((1, right[1] - right[0]))
        ret.add((-1, right[1] + right[0]))
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
#    for s in sensors:
#        if s.beacon[1] == y and s.beacon[0] in coverage:
#            print('removing beacon at', s.beacon)
#            coverage.remove(s.beacon[0])
    return coverage

def print_coverage(sensors, x1, y1, x2, y2, coverage, y):
    for j in range(y1, y2):
        for i in range(x1, x2):
            pass

sensors = parse_sensors(sys.stdin.readlines())
#for s in sensors:
#    print(vars(s))

# identify all overlapping bounds across all sensors
# the intersection of these overlaps is where the
# distress beacon will be
def bounds_intersections(sensors):
    matching_bounds = set()
    for s in sensors:
        print(s.mdist, s.get_bounds())
        for t in sensors:
            if s == t:
                continue
            i = set.intersection(s.get_bounds(), t.get_bounds())
            matching_bounds.update(i)
    print(matching_bounds)

    #find intersections of the matching bounds
    ipoints = []
    for a in matching_bounds:
        # make a always the neg slope
        if a[0] == 1:
            continue
        for b in matching_bounds:
            if a != b and b[0] == 1:
                s = (a[1] - b[1])
                if s % 2 == 1:
                    print('something wrong! non-integer intersection point! ignoring...')
                else:
                    x = int(s/2)
                    y = -x + a[1]
#                print(a, b, (x,y))
                    ipoints.append((x,y))
#    print(ipoints)
    return ipoints

# for each intersection, test whether it is outside the
# manhattan distance for all sensors
def test_ipoints(sensors, ipoints, max_coord):
    ret = []
    for i in ipoints:
        if i[0] < 0 or i[0] > max_coord:
            continue
        elif i[1] < 0 or i[1] > max_coord:
            continue
        else:
            too_close = False
            for s in sensors:
                if Sensor.calc_mdist(s.loc, i) <= s.mdist:
                    too_close = True
                    break
            if not too_close:
                ret.append(i)
    print(ret)
    if len(ret) == 1:
        answer = ret[0]
        print(answer[0]*4000000+answer[1])

ipoints = bounds_intersections(sensors)
test_ipoints(sensors, ipoints, 4000000)
    
def brute(sensors, dimensions):
    x = y = dimensions
    setx = set(range(x))
    for j in range(y):
        if j % 10 == 0:
            print('testing row',j)
        coverage = get_line_coverage(sensors, j)
        diff = setx - coverage
        if len(diff) != 0:
            x = list(diff)[0]
            print(x, j)

