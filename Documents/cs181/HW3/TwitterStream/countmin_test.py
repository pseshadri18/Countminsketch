from countmin import CountMin

def main():
    delta = 0.001 # for width 
    epsilon = .2 # for depth

    # make sure increment and estimate work 
    cm = CountMin(epsilon, delta)
    cm1 = CountMin(epsilon, delta)
    if (cm.width == 3 and cm.depth == 10):
        print 'correct dimensions'
    else:
        print 'issue with dimensions'

    # words to use for testing     
    w1 = 'hi'
    w2 = 'good'
    w3 = 'morning'
    w4 = 'bye'
    w5 = 'night'

    # test increment and estimate
    cm.increment(w1)
    cm.increment(w2)
    cm.increment(w2)
    cm.increment(w2)
    cm.increment(w4)
    cm.increment(w4)


    if (cm.estimate(w1) == 1 and cm.estimate(w2) == 3 and cm.estimate(w3) == 0 and cm.estimate(w4) == 2):
        print 'increment/estimate look good'
    else:
        print 'there is an issue in increment/estimate'
    
    cm1.increment(w5)
    cm1.increment(w5)
    cm1.increment(w3)
    cm1.increment(w1)
    cm1.increment(w2)

    cm3 = cm.merge(cm1)

    # test merge
    if (cm3.estimate(w1) == 2 and cm3.estimate(w2) == 4 and cm3.estimate(w3) == 1 and cm3.estimate(w4) == 2 and cm3.estimate(w5) == 2):
        print 'merge looks good'
    else:
        print 'there is an issue in merge'

if __name__ == '__main__':
    main()