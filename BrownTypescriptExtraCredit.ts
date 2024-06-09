import * as fs from 'fs';
import * as csv from 'csv-parse';

class Cell {
  oem: string | null;
  model: string | null;
  launchAnnounced: number | null;
  launchStatus: string | null;
  bodyDimensions: string | null;
  bodyWeight: number | null;
  bodySim: string | null;
  displayType: string | null;
  displaySize: number | null;
  displayResolution: string | null;
  featuresSensors: string | null;
  platformOs: string | null;

  constructor(data: string[]) {
    // I assign the values from the data array to the corresponding properties
    // I replace missing or invalid values with null
    this.oem = data[0] || null;
    this.model = data[1] || null;
    this.launchAnnounced = data[2] ? parseInt(data[2]) : null;
    this.launchStatus = data[3] || null;
    this.bodyDimensions = data[4] || null;
    this.bodyWeight = data[5] ? parseFloat(data[5].replace(/[^0-9.]/g, '')) : null;
    this.bodySim = data[6] === 'No' ? null : data[6];
    this.displayType = data[7] || null;
    this.displaySize = data[8] ? parseFloat(data[8]) : null;
    this.displayResolution = data[9] || null;
    this.featuresSensors = data[10] || null;
    this.platformOs = data[11] ? data[11].split(',')[0].trim() : null;
  }

  // I add my methods here
}

// I create three data structures to store the Cell objects
const cells: Cell[] = [];
const cellMap = new Map<string, Cell>();
const cellSet = new Set<Cell>();

fs.createReadStream('cell_phones.csv')
  .pipe(csv())
  .on('data', (data: string[]) => {
    // I create a new Cell object for each row in the CSV file
    const cell = new Cell(data);
    // I add the Cell object to my data structures
    cells.push(cell);
    cellMap.set(cell.model || '', cell);
    cellSet.add(cell);
  })
  .on('end', () => {
    // I perform operations and tests on the data here
    console.log('Data ingestion completed.');

    // I test if the file is not empty
    if (cells.length === 0) {
      throw new Error('The input file is empty.');
    }

    // I test if display_size is now a float
    cells.forEach((cell) => {
      if (cell.displaySize !== null && typeof cell.displaySize !== 'number') {
        throw new Error('Display size is not a float.');
      }
    });

    // I test if all missing or "-" data is replaced with null
    cells.forEach((cell) => {
      Object.values(cell).forEach((value) => {
        if (value === '-') {
          throw new Error('Missing or "-" data is not replaced with null.');
        }
      });
    });

toString(): string { 
return `OEM: ${this.oem}, Model: ${this.model}, Launch Announced: ${this.launchAnnounced}, Launch Status: ${this.launchStatus}`; } 
getBodyWeightInGrams(): number | null { 
return this.bodyWeight; } 
hasMultipleFeatureSensors(): boolean { 
return this.featuresSensors !== null && this.featuresSensors.split(',').length > 1; } }
on('end', () => { 
// I perform operations and tests on the data here 
console.log('Data ingestion completed.'); // ... (previous tests remain the same) 
// I calculate the average phone body weight for each OEM 
const oemWeightMap = new Map<string, { sum: number; count: number }>(); 
cells.forEach((cell) => { if (cell.oem !== null && cell.bodyWeight !== null) {
 const oemData = oemWeightMap.get(cell.oem) || { sum: 0, count: 0 }; 
oemData.sum += cell.bodyWeight; oemData.count++; 
oemWeightMap.set(cell.oem, oemData);

  });

