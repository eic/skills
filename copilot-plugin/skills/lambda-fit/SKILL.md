---
name: lambda-fit
description: Reconstruct and fit the Lambda0 -> p pi- invariant-mass peak in ePIC EDM4eic data through the EIC MCP servers. Worked example from the tutorial https://eic.github.io/tutorial-mcp/.
---

# Lambda Invariant-Mass Fit

Use this skill to measure the Lambda0 (or anti-Lambda0) yield, mass, or width in ePIC reconstructed data with the uproot, xrootd, and rucio MCP servers. It is the worked example from the [MCP tutorial](https://eic.github.io/tutorial-mcp/).

## Procedure

1. Check the input files with the uproot tool `validate_dataset_schema`.
2. Histogram m(p pi-) and m(pbar pi+) over [1.08, 1.16] GeV in 80 bins and return the counts and their sum; use `execute_kernel` for one file and `execute_kernel_dataset` with `reduce_code` for many, at most 10 files per call.
3. Fit each histogram in one more `execute_kernel` call with a Gaussian plus 2nd-order polynomial; scan mu and sigma on a grid and solve the other four parameters by weighted linear least squares.
4. Report mu, sigma, the yield S = A sqrt(2 pi) sigma / bin width, and chi2/ndf, with uncertainties.
5. List the dataset DID, the files used, and the tool calls with their arguments.

## Constraints

- The entries in the fitted histogram must equal the sum returned by the histogram step; if not, counts were lost in copying and the fit is redone.
- With fewer than 50 entries, report insufficient statistics and stop.
- Accept a fit only if |mu - 1.115683 GeV| < 0.005 GeV, sigma is in [0.001, 0.005] GeV, and chi2/ndf is between 0.5 and 1.5.
- If any check fails, report the failure and the fit numbers, not a result.
- Read files only through the uproot MCP tools; a file's URL is `root://epicxrd1.sdcc.bnl.gov:1095//eic/EPIC` followed by its rucio name.

## Inputs

- `root_file_url_or_dataset_did`
- `number_of_files`

## Outputs

- `fit_parameters`
- `success_checks`
- `provenance`

## Example

- **Prompt:** Using the lambda-fit skill, measure the Lambda0 and anti-Lambda0 peaks in the first 30 files of the campaign 26.04.1 BeAGLE eCu ep 10x115 reconstructed-DIS dataset.
- **Outcome:** mu, sigma, yield, and chi2/ndf for both peaks with the success checks, the dataset DID, the file list, and the tool calls.
