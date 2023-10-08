import os
import pandas as pd
import itertools

os.system('cls')

# INFO
# takes post codes and stores in set
# creates combinations of pair of codes

filePath = r'C:\Users\Damian\pyproj\PostCodes\PostCodes.xlsx'
sheetName = 'FEED'
columnName = 'L2_UNIQCODE'
inputDataFrame = pd.read_excel(filePath, sheet_name=sheetName)
print(inputDataFrame.head())

uniqueCodes = set()
for postCode in inputDataFrame[columnName]:
    uniqueCodes.add(postCode)

numberOfUniqueCodes = len(uniqueCodes)
numberOfPairCombinations = numberOfUniqueCodes * (numberOfUniqueCodes - 1) / 2
print('Pair combinations: C = N * (N - 1) / 2')
print(f'N = {numberOfUniqueCodes}')
print(f'C = {int(numberOfPairCombinations)}')

uniquePairs = set(itertools.combinations(uniqueCodes, 2))

outputDataFrame = pd.DataFrame(uniquePairs, columns=['Code1','Code2'])
print(outputDataFrame.head())
print(outputDataFrame.info())

outputPath = r'C:\Users\Damian\pyproj\PostCodes\UniquePairsOfPostCodes.xlsx'
outputDataFrame.to_excel(outputPath, index=False)
print(f'Data saved: {outputPath}')
