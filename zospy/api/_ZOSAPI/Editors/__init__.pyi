"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from zospy.api._ZOSAPI.Editors.LDE import SurfaceColumn
from zospy.api._ZOSAPI.Editors.NCE import ObjectColumn
from zospy.api._ZOSAPI.SystemData import FieldColumn

from . import LDE, MCE, MFE, NCE, TDE

__all__ = (
    "LDE",
    "MCE",
    "MFE",
    "NCE",
    "TDE",
    "CellDataType",
    "EditorType",
    "IEditor",
    "IEditor",
    "IEditorCell",
    "IEditorCell",
    "IEditorRow",
    "IEditorRow",
    "ISolveAplanatic",
    "ISolveAutomatic",
    "ISolveCenterOfCurvature",
    "ISolveChiefRayAngle",
    "ISolveChiefRayHeight",
    "ISolveChiefRayNormal",
    "ISolveCocentricRadius",
    "ISolveCocentricSurface",
    "ISolveCompensator",
    "ISolveConfigPickup",
    "ISolveData",
    "ISolveData",
    "ISolveDuplicateSag",
    "ISolveDuplicateSag",
    "ISolveEdgeThickness",
    "ISolveElementPower",
    "ISolveFieldPickup",
    "ISolveFixed",
    "ISolveFNumber",
    "ISolveInvertSag",
    "ISolveInvertSag",
    "ISolveMarginalRayAngle",
    "ISolveMarginalRayHeight",
    "ISolveMarginalRayNormal",
    "ISolveMaterialModel",
    "ISolveMaterialOffset",
    "ISolveMaterialSubstitute",
    "ISolveMaximum",
    "ISolveNone",
    "ISolveObjectPickup",
    "ISolveOpticalPathDifference",
    "ISolvePickupChiefRay",
    "ISolvePosition",
    "ISolvePupilPosition",
    "ISolveSurfacePickup",
    "ISolveThermalPickup",
    "ISolveVariable",
    "ISolveZPLMacro",
    "ReflectTransmitCode",
    "SampleSides",
    "Samplings",
    "SolveStatus",
    "SolveType",
)

class CellDataType:
    Integer = 0
    Double = 1
    String = 2

class EditorType:
    LDE = 0
    NCE = 1
    MFE = 2
    TDE = 3
    MCE = 4

class IEditor:
    def AddRow(self) -> IEditorRow: ...
    def DeleteAllRows(self) -> int: ...
    def DeleteRowAt(self, pos: int) -> bool: ...
    def DeleteRowsAt(self, pos: int, numberOfRows: int) -> int: ...
    @property
    def Editor(self) -> EditorType: ...
    @property
    def MaxColumn(self) -> int: ...
    @property
    def MinColumn(self) -> int: ...
    @property
    def NumberOfRows(self) -> int: ...
    def GetRowAt(self, pos: int) -> IEditorRow: ...
    def HideEditor(self) -> None: ...
    def InsertRowAt(self, pos: int) -> IEditorRow: ...
    def ShowEditor(self) -> bool: ...

class IEditorCell:
    def CreateSolveType(self, type: SolveType) -> ISolveData: ...
    def FillAvailableSolveTypes(self, Length: int) -> tuple[list[SolveType]]: ...
    @property
    def Col(self) -> int: ...
    @property
    def DataType(self) -> CellDataType: ...
    @property
    def DoubleValue(self) -> float: ...
    @property
    def Header(self) -> str: ...
    @property
    def IntegerValue(self) -> int: ...
    @property
    def IsActive(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Row(self) -> IEditorRow: ...
    @property
    def Solve(self) -> SolveType: ...
    @property
    def Value(self) -> str: ...
    def GetAvailableSolveTypes(self) -> list[SolveType]: ...
    def GetNumberOfSolveTypes(self) -> int: ...
    def GetSolveData(self) -> ISolveData: ...
    def IsSolveTypeSupported(self, st: SolveType) -> bool: ...
    def MakeSolveFixed(self) -> bool: ...
    def MakeSolveVariable(self) -> bool: ...
    @DoubleValue.setter
    def DoubleValue(self, value: float) -> None: ...
    @IntegerValue.setter
    def IntegerValue(self, value: int) -> None: ...
    @Value.setter
    def Value(self, value: str) -> None: ...
    def SetSolveData(self, Data: ISolveData) -> SolveStatus: ...

class IEditorRow:
    @property
    def Bookmark(self) -> str: ...
    @property
    def Editor(self) -> IEditor: ...
    @property
    def IsValidRow(self) -> bool: ...
    @property
    def RowIndex(self) -> int: ...
    @property
    def RowTypeName(self) -> str: ...
    def GetCellAt(self, pos: int) -> IEditorCell: ...
    @Bookmark.setter
    def Bookmark(self, value: str) -> None: ...

class ISolveAplanatic(ISolveData):
    pass

class ISolveAutomatic(ISolveData):
    pass

class ISolveCenterOfCurvature(ISolveData):
    @property
    def RefSurface(self) -> int: ...
    @RefSurface.setter
    def RefSurface(self, value: int) -> None: ...

class ISolveChiefRayAngle(ISolveData):
    @property
    def Angle(self) -> float: ...
    @Angle.setter
    def Angle(self, value: float) -> None: ...

class ISolveChiefRayHeight(ISolveData):
    @property
    def Height(self) -> float: ...
    @Height.setter
    def Height(self, value: float) -> None: ...

class ISolveChiefRayNormal(ISolveData):
    pass

class ISolveCocentricRadius(ISolveData):
    @property
    def WithSurface(self) -> int: ...
    @WithSurface.setter
    def WithSurface(self, value: int) -> None: ...

class ISolveCocentricSurface(ISolveData):
    @property
    def AboutSurface(self) -> int: ...
    @AboutSurface.setter
    def AboutSurface(self, value: int) -> None: ...

class ISolveCompensator(ISolveData):
    @property
    def RefSurface(self) -> int: ...
    @property
    def Sum(self) -> float: ...
    @RefSurface.setter
    def RefSurface(self, value: int) -> None: ...
    @Sum.setter
    def Sum(self, value: float) -> None: ...

class ISolveConfigPickup(ISolveData):
    @property
    def Configuration(self) -> int: ...
    @property
    def Offset(self) -> float: ...
    @property
    def Operand(self) -> int: ...
    @property
    def ScaleFactor(self) -> float: ...
    @property
    def SupportsOffset(self) -> bool: ...
    @property
    def SupportsScale(self) -> bool: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...
    @Offset.setter
    def Offset(self, value: float) -> None: ...
    @Operand.setter
    def Operand(self, value: int) -> None: ...
    @ScaleFactor.setter
    def ScaleFactor(self, value: float) -> None: ...

class ISolveData:
    @property
    def _S_Aplanatic(self) -> ISolveAplanatic: ...
    @property
    def _S_Automatic(self) -> ISolveAutomatic: ...
    @property
    def _S_CenterOfCurvature(self) -> ISolveCenterOfCurvature: ...
    @property
    def _S_ChiefRayAngle(self) -> ISolveChiefRayAngle: ...
    @property
    def _S_ChiefRayHeight(self) -> ISolveChiefRayHeight: ...
    @property
    def _S_ChiefRayNormal(self) -> ISolveChiefRayNormal: ...
    @property
    def _S_CocentricRadius(self) -> ISolveCocentricRadius: ...
    @property
    def _S_CocentricSurface(self) -> ISolveCocentricSurface: ...
    @property
    def _S_Compensator(self) -> ISolveCompensator: ...
    @property
    def _S_ConfigPickup(self) -> ISolveConfigPickup: ...
    @property
    def _S_DuplicateSag(self) -> ISolveDuplicateSag: ...
    @property
    def _S_EdgeThickness(self) -> ISolveEdgeThickness: ...
    @property
    def _S_ElementPower(self) -> ISolveElementPower: ...
    @property
    def _S_FieldPickup(self) -> ISolveFieldPickup: ...
    @property
    def _S_Fixed(self) -> ISolveFixed: ...
    @property
    def _S_FNumber(self) -> ISolveFNumber: ...
    @property
    def _S_InvertSag(self) -> ISolveInvertSag: ...
    @property
    def _S_MarginalRayAngle(self) -> ISolveMarginalRayAngle: ...
    @property
    def _S_MarginalRayHeight(self) -> ISolveMarginalRayHeight: ...
    @property
    def _S_MarginalRayNormal(self) -> ISolveMarginalRayNormal: ...
    @property
    def _S_MaterialModel(self) -> ISolveMaterialModel: ...
    @property
    def _S_MaterialOffset(self) -> ISolveMaterialOffset: ...
    @property
    def _S_MaterialSubstitute(self) -> ISolveMaterialSubstitute: ...
    @property
    def _S_Maximum(self) -> ISolveMaximum: ...
    @property
    def _S_None(self) -> ISolveNone: ...
    @property
    def _S_ObjectPickup(self) -> ISolveObjectPickup: ...
    @property
    def _S_OpticalPathDifference(self) -> ISolveOpticalPathDifference: ...
    @property
    def _S_PickupChiefRay(self) -> ISolvePickupChiefRay: ...
    @property
    def _S_Position(self) -> ISolvePosition: ...
    @property
    def _S_PupilPosition(self) -> ISolvePupilPosition: ...
    @property
    def _S_SurfacePickup(self) -> ISolveSurfacePickup: ...
    @property
    def _S_ThermalPickup(self) -> ISolveThermalPickup: ...
    @property
    def _S_Variable(self) -> ISolveVariable: ...
    @property
    def _S_ZPLMacro(self) -> ISolveZPLMacro: ...
    @property
    def IsValid(self) -> bool: ...
    @property
    def Type(self) -> SolveType: ...

class ISolveDuplicateSag:
    @property
    def Surface(self) -> int: ...
    @Surface.setter
    def Surface(self, value: int) -> None: ...

class ISolveEdgeThickness(ISolveData):
    @property
    def RadialHeight(self) -> float: ...
    @property
    def Thickness(self) -> float: ...
    @RadialHeight.setter
    def RadialHeight(self, value: float) -> None: ...
    @Thickness.setter
    def Thickness(self, value: float) -> None: ...

class ISolveElementPower(ISolveData):
    @property
    def Power(self) -> float: ...
    @Power.setter
    def Power(self, value: float) -> None: ...

class ISolveFieldPickup(ISolveData):
    @property
    def Column(self) -> FieldColumn: ...
    @property
    def Field(self) -> int: ...
    @property
    def Offset(self) -> float: ...
    @property
    def ScaleFactor(self) -> float: ...
    def IsPickupFromCurrentColumn(self) -> bool: ...
    def MakePickupFromCurrentColumn(self) -> None: ...
    @Column.setter
    def Column(self, value: FieldColumn) -> None: ...
    @Field.setter
    def Field(self, value: int) -> None: ...
    @Offset.setter
    def Offset(self, value: float) -> None: ...
    @ScaleFactor.setter
    def ScaleFactor(self, value: float) -> None: ...

class ISolveFixed(ISolveData):
    pass

class ISolveFNumber(ISolveData):
    @property
    def FNumber(self) -> float: ...
    @FNumber.setter
    def FNumber(self, value: float) -> None: ...

class ISolveInvertSag:
    @property
    def Surface(self) -> int: ...
    @Surface.setter
    def Surface(self, value: int) -> None: ...

class ISolveMarginalRayAngle(ISolveData):
    @property
    def Angle(self) -> float: ...
    @Angle.setter
    def Angle(self, value: float) -> None: ...

class ISolveMarginalRayHeight(ISolveData):
    @property
    def Height(self) -> float: ...
    @property
    def PupilZone(self) -> float: ...
    @Height.setter
    def Height(self, value: float) -> None: ...
    @PupilZone.setter
    def PupilZone(self, value: float) -> None: ...

class ISolveMarginalRayNormal(ISolveData):
    pass

class ISolveMaterialModel(ISolveData):
    @property
    def AbbeVd(self) -> float: ...
    @property
    def dPgF(self) -> float: ...
    @property
    def IndexNd(self) -> float: ...
    @property
    def VaryAbbe(self) -> bool: ...
    @property
    def VarydPgF(self) -> bool: ...
    @property
    def VaryIndex(self) -> bool: ...
    @AbbeVd.setter
    def AbbeVd(self, value: float) -> None: ...
    @dPgF.setter
    def dPgF(self, value: float) -> None: ...
    @IndexNd.setter
    def IndexNd(self, value: float) -> None: ...
    @VaryAbbe.setter
    def VaryAbbe(self, value: bool) -> None: ...
    @VarydPgF.setter
    def VarydPgF(self, value: bool) -> None: ...
    @VaryIndex.setter
    def VaryIndex(self, value: bool) -> None: ...

class ISolveMaterialOffset(ISolveData):
    @property
    def NdOffset(self) -> float: ...
    @property
    def VdOffset(self) -> float: ...
    @NdOffset.setter
    def NdOffset(self, value: float) -> None: ...
    @VdOffset.setter
    def VdOffset(self, value: float) -> None: ...

class ISolveMaterialSubstitute(ISolveData):
    @property
    def Catalog(self) -> str: ...
    @Catalog.setter
    def Catalog(self, value: str) -> None: ...

class ISolveMaximum(ISolveData):
    pass

class ISolveNone(ISolveData):
    pass

class ISolveObjectPickup(ISolveData):
    @property
    def Column(self) -> ObjectColumn: ...
    @property
    def Object(self) -> int: ...
    @property
    def Offset(self) -> float: ...
    @property
    def ScaleFactor(self) -> float: ...
    @property
    def SupportsOffset(self) -> bool: ...
    @property
    def SupportsScale(self) -> bool: ...
    def IsPickupFromCurrentColumn(self) -> bool: ...
    def MakePickupFromCurrentColumn(self) -> None: ...
    @Column.setter
    def Column(self, value: ObjectColumn) -> None: ...
    @Object.setter
    def Object(self, value: int) -> None: ...
    @Offset.setter
    def Offset(self, value: float) -> None: ...
    @ScaleFactor.setter
    def ScaleFactor(self, value: float) -> None: ...

class ISolveOpticalPathDifference(ISolveData):
    @property
    def OPD(self) -> float: ...
    @property
    def PupilZone(self) -> float: ...
    @OPD.setter
    def OPD(self, value: float) -> None: ...
    @PupilZone.setter
    def PupilZone(self, value: float) -> None: ...

class ISolvePickupChiefRay(ISolveData):
    @property
    def Field(self) -> int: ...
    @property
    def Wavelength(self) -> int: ...
    @Field.setter
    def Field(self, value: int) -> None: ...
    @Wavelength.setter
    def Wavelength(self, value: int) -> None: ...

class ISolvePosition(ISolveData):
    @property
    def FromSurface(self) -> int: ...
    @property
    def Length(self) -> float: ...
    @FromSurface.setter
    def FromSurface(self, value: int) -> None: ...
    @Length.setter
    def Length(self, value: float) -> None: ...

class ISolvePupilPosition(ISolveData):
    pass

class ISolveSurfacePickup(ISolveData):
    @property
    def Column(self) -> SurfaceColumn: ...
    @property
    def Offset(self) -> float: ...
    @property
    def ScaleFactor(self) -> float: ...
    @property
    def SupportsOffset(self) -> bool: ...
    @property
    def SupportsScale(self) -> bool: ...
    @property
    def Surface(self) -> int: ...
    def IsPickupFromCurrentColumn(self) -> bool: ...
    def MakePickupFromCurrentColumn(self) -> None: ...
    @Column.setter
    def Column(self, value: SurfaceColumn) -> None: ...
    @Offset.setter
    def Offset(self, value: float) -> None: ...
    @ScaleFactor.setter
    def ScaleFactor(self, value: float) -> None: ...
    @Surface.setter
    def Surface(self, value: int) -> None: ...

class ISolveThermalPickup(ISolveData):
    @property
    def Configuration(self) -> int: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...

class ISolveVariable(ISolveData):
    pass

class ISolveZPLMacro(ISolveData):
    @property
    def Macro(self) -> str: ...
    def GetAvailableMacros(self) -> list[str]: ...
    @Macro.setter
    def Macro(self, value: str) -> None: ...

class ReflectTransmitCode:
    Success = 0
    NoReflectDataInFile = 1
    NoTransmitDataInFile = 2

class SampleSides:
    Front = 0
    Back = 1

class Samplings:
    FiveDegrees = 0
    TwoDegrees = 1
    OneDegree = 2

class SolveStatus:
    Success = 0
    InvalidSolveType = 1
    InvalidRow = 2
    InvalidColumn = 3
    PostSurfaceStopOnly = 4
    InvalidMacro = 5
    Failed = 10000

class SolveType:
    # None = 0
    Fixed = 1
    Variable = 2
    SurfacePickup = 3
    ZPLMacro = 4
    MarginalRayAngle = 5
    MarginalRayHeight = 6
    ChiefRayAngle = 7
    MarginalRayNormal = 8
    ChiefRayNormal = 9
    Aplanatic = 10
    ElementPower = 11
    CocentricSurface = 12
    ConcentricSurface = 12
    CocentricRadius = 13
    ConcentricRadius = 13
    FNumber = 14
    ChiefRayHeight = 15
    EdgeThickness = 16
    OpticalPathDifference = 17
    Position = 18
    Compensator = 19
    CenterOfCurvature = 20
    PupilPosition = 21
    MaterialSubstitute = 22
    MaterialOffset = 23
    MaterialModel = 24
    Automatic = 25
    Maximum = 26
    PickupChiefRay = 27
    ObjectPickup = 28
    ConfigPickup = 29
    ThermalPickup = 30
    MarginPercent = 31
    CA_fill = 32
    DIA_fill = 33
    DuplicateSag = 34
    InvertSag = 35
    FieldPickup = 10000
