#!/usr/bin/env python
import os
import sys
import commands

BLOCK_SIZE = 4096
#AdjustPartitionSizeForVerity.results = {}


def GetVerityMetadataSize(partition_size):
  cmd = "./bin/build_verity_metadata.py -s %d"
  cmd %= partition_size

  status, output = commands.getstatusoutput(cmd)
  if status:
    print output
    return False, 0
  return True, int(output)

def GetVerityFECSize(partition_size):
  cmd = "./bin/fec -s %d" % partition_size
  status, output = commands.getstatusoutput(cmd)
  if status:
    print output
    return False, 0
  return True, int(output)

def GetVeritySize(partition_size, fec_supported):
  success, verity_tree_size = GetVerityTreeSize(partition_size)
  if not success:
    return 0
  success, verity_metadata_size = GetVerityMetadataSize(partition_size)
  if not success:
    return 0
  verity_size = verity_tree_size + verity_metadata_size
  if fec_supported:
    success, fec_size = GetVerityFECSize(partition_size + verity_size)
    if not success:
      return 0
    return verity_size + fec_size
  return verity_size

def GetVerityTreeSize(partition_size):
  cmd = "./bin/build_verity_tree -s %d"
  cmd %= partition_size
  status, output = commands.getstatusoutput(cmd)
  if status:
    print output
    return False, 0
  return True, int(output)


def AdjustPartitionSizeForVerity(partition_size, fec_supported):
  """Modifies the provided partition size to account for the verity metadata.

  This information is used to size the created image appropriately.
  Args:
    partition_size: the size of the partition to be verified.
  Returns:
    The size of the partition adjusted for verity metadata.
  """
#  key = "%d %d" % (partition_size, 	fec_supported)
#  if key in AdjustPartitionSizeForVerity.results:
#    return AdjustPartitionSizeForVerity.results[key]

  hi = partition_size
  if hi % BLOCK_SIZE != 0:
    hi = (hi // BLOCK_SIZE) * BLOCK_SIZE

  # verity tree and fec sizes depend on the partition size, which
  # means this estimate is always going to be unnecessarily small
  lo = partition_size - GetVeritySize(hi, fec_supported)
  result = lo

  # do a binary search for the optimal size
  while lo < hi:
    i = ((lo + hi) // (2 * BLOCK_SIZE)) * BLOCK_SIZE
    size = i + GetVeritySize(i, fec_supported)
    if size <= partition_size:
      if result < i:
        result = i
      lo = i + BLOCK_SIZE
    else:
      hi = i

#  AdjustPartitionSizeForVerity.results[key] = result
  return result

def main(argv):
    size = int(argv[1])
    print AdjustPartitionSizeForVerity(size,1)
    sys.exit(1)

if __name__ == '__main__':
  main(sys.argv[0:])
