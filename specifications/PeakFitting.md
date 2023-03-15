<h2 align="center">
  Data model for the peak fitting algorithm
</h2>

---------
# Dataset

This is the place where you can describe the complete module/dataset and give information about all the details. Markdown offers a convenient way to enable as much space as needed to elucidate purpose and capabilities of your data model.

## Objects

### Root

This is the root of the data model and contains all objects defined in this example. While its good practice to have a single root, you can define as many roots as you like. Furthermore, the name does not have to be ```Root``` and can be any other name.

- description
  - Type: string
  - Description: Describes the content of the dataset.
- title
  - Type: string
  - Description: Title of the work
- subject
  - Type: string
  - Description: Subject of matter linked to the dataset
  - Multiple: True
- authors
  - Type: Author
  - Multiple: True
  - Description: Authors of this dataset.
- analysis
  - Type: Analysis
  - Description: analysis part of this dataset.

### Author

This is another object that represents the author of the dataset. Please note, that the options here contain all required fields but also custom ones. In this example, the ```Dataverse``` option specifies where each field should be mapped, when exported to a Dataverse format. Hence, these options allow you to link your dataset towards any other data model without writing code by yourself.

- name
  - Type: string
  - Description: Full name including given and family name
  - Dataverse: pyDaRUS.Citation.author.name
- affiliation
  - Type: string
  - Description: To which organization the author is affiliated to

### Analysis
- metadata
  - Type: Metadata
  - Description: metadata of the corresponding measuring data.
- experimental_data
  - Type: ExperimentalData
  - Description: experimental data of a measurement.

### Metadata
- IR
  - Type: IR
  - Description: IR measurement.
- XRD
  - Type: XRD
  - Description: XRD measurement.
- GC
  - Type: GC
  - Description: GC measurement.
- NMR
  - Type: NMR
  - Description: NMR measurement.

### IR
- placeholder
  - Type: string
  - Description: placeholder

### XRD
- placeholder
  - Type: string
  - Description: placeholder

### GC
- placeholder
  - Type: string
  - Description: placeholder

### NMR
- placeholder
  - Type: string
  - Description: placeholder

### ExperimentalData
- x_values
  - Type: float
  - Multiple: True
  - Description: x values of the experimental data e.g. time or angle.
- x_unit
  - Type: Units
  - Description: unit of the x values e.g. mm or degree.
- y_matrix
  - Type: YMatrix
  - Multiple: True
  - Description: array of y values of corresponding x values.

### YMatrix
- y_values
  - Type: float
  - Multiple: True
  - Description: y values of the experimental data e.g. concentration or intensity.
- y_unit
  - Type: Units
  - Description: unit of the y values e.g. mol per l or arbitrary units


## Enumerations

### Units
```python
SECONDS = "s"
DEGREE = "degree"
PPM = "ppm"
NANOMETER = "nm"
RECIPROCALCENTIMETER = "reciprocal centimeter"
MOLPERLITER = "mol per liter"
ARBITRARYUNIT = "a.u."
```