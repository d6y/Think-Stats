import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

live_births = [r for r in table.records if r.outcome == 1]
print 'Live births:', len(live_births)

first_live_birth = [r for r in live_births if r.birthord == 1]
other_live_birth = [r for r in live_births if r.birthord != 1]
print 'First births:', len(first_live_birth)
print 'Others:', len(other_live_birth)

def mean(xs):
	return sum(xs) / float(len(xs))	

def preg_len(p):
	return p.prglength


mean_first = mean( map(preg_len, first_live_birth) )
mean_other = mean( map(preg_len, other_live_birth) )

print 'Mean duration first birth in weeks', mean_first
print 'Mean duration other birth', mean_other

hours_diff = (mean_first - mean_other) * 7.0 * 24.0
print 'Hours difference:', hours_diff