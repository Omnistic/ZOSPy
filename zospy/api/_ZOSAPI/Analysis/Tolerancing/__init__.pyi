"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from zospy.api._ZOSAPI.Analysis.Settings import IAS_, IAS_Field, IAS_Wavelength
from zospy.api._ZOSAPI.Analysis.Tolerancing.QuickYield import IAS_QYField
from zospy.api._ZOSAPI.Tools.Tolerancing import MonteCarloStatistics

from . import QuickYield

__all__ = (
    "QuickYield",
    "IAS_QuickYield",
    "IAS_TolerancingHistogram",
    "IAS_TolerancingYield",
    "ITolerancingOperand",
    "ITolerancingOperand",
    "ITolerancingOperands",
    "ITolerancingOperands",
    "QYCompensations",
    "QYCompensatorStrategy",
    "QYPrecisions",
)

class IAS_QuickYield(IAS_):
    @property
    def Compensation(self) -> QYCompensations: ...
    @property
    def CompensatorStrategy(self) -> QYCompensatorStrategy: ...
    @property
    def Configuration(self) -> int: ...
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def NumMonteCarlo(self) -> int: ...
    @property
    def Precision(self) -> QYPrecisions: ...
    @property
    def PupilSampling(self) -> int: ...
    @property
    def QYField(self) -> IAS_QYField: ...
    @property
    def Statistic(self) -> MonteCarloStatistics: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @Compensation.setter
    def Compensation(self, value: QYCompensations) -> None: ...
    @CompensatorStrategy.setter
    def CompensatorStrategy(self, value: QYCompensatorStrategy) -> None: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...
    @NumMonteCarlo.setter
    def NumMonteCarlo(self, value: int) -> None: ...
    @Precision.setter
    def Precision(self, value: QYPrecisions) -> None: ...
    @PupilSampling.setter
    def PupilSampling(self, value: int) -> None: ...
    @Statistic.setter
    def Statistic(self, value: MonteCarloStatistics) -> None: ...

class IAS_TolerancingHistogram(IAS_):
    @property
    def Filename(self) -> str: ...
    @property
    def MaxValue(self) -> float: ...
    @property
    def MinValue(self) -> float: ...
    @property
    def NumBins(self) -> int: ...
    @property
    def Operand(self) -> int: ...
    def GetOperands(self) -> ITolerancingOperands: ...
    def GetToleranceFiles(self) -> list[str]: ...
    @Filename.setter
    def Filename(self, value: str) -> None: ...
    @MaxValue.setter
    def MaxValue(self, value: float) -> None: ...
    @MinValue.setter
    def MinValue(self, value: float) -> None: ...
    @NumBins.setter
    def NumBins(self, value: int) -> None: ...
    @Operand.setter
    def Operand(self, value: int) -> None: ...
    def UseSystemTolerances(self) -> None: ...

class IAS_TolerancingYield(IAS_):
    @property
    def Filename(self) -> str: ...
    @property
    def Operand(self) -> int: ...
    def GetOperands(self) -> ITolerancingOperands: ...
    def GetToleranceFiles(self) -> list[str]: ...
    @Filename.setter
    def Filename(self, value: str) -> None: ...
    @Operand.setter
    def Operand(self, value: int) -> None: ...
    def UseSystemTolerances(self) -> None: ...

class ITolerancingOperand:
    @property
    def OperandName(self) -> str: ...
    @property
    def ParameterData(self) -> str: ...

class ITolerancingOperands:
    @property
    def NumberOfOperands(self) -> int: ...
    @property
    def Operands(self) -> list[ITolerancingOperand]: ...
    def GetOperand(self, operandIndex: int) -> ITolerancingOperand: ...

class QYCompensations:
    Standard = 0
    High = 1
    VeryHigh = 2

class QYCompensatorStrategy:
    OptimizeAllDampedLeastSquares = 0
    ParaxialFocus = 1
    Ignore = 2
    OptimizeAllOrthogonalDescent = 3

class QYPrecisions:
    Standard = 0
    High = 1
    VeryHigh = 2