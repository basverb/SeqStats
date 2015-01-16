def fasta(filename):
  try:
    f = file(filename)
  except IOError:                     
    print "The file, %s, does not exist" % filename
    return

  order = []
  sequences = {}
    
  for line in f:
    if line.startswith('>'):
        name = line[1:].rstrip('\n')
        name = name.replace('_', ' ')
        order.append(name)
        sequences[name] = ''
    else:
        sequences[name] += line.rstrip('\n').rstrip('*')
            
  print "%d sequence(s) found" % len(order)          
  print order
  print sequences
  return order,sequences
fasta('sequence.fasta')
