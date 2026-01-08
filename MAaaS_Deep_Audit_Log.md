# MAaaS PLATFORM AUDIT - DEEP SCAN
Scan Root: C:\Users\PC\MAaaS
=================================

📂 **ROOT/**
    📄 `.cursorrules`
    📄 `.gitignore`
    📄 `api_server.py`
        > *Code Insight:*
        ```python
        Provides programmatic access to the Swarm Agency ecosystem.
        ```
    📄 `CHAT_OPS_INTEGRATION.md`
        > *Code Insight:*
        ```python
        # Chat Ops Integration - Real Agent Communication
        ```
    📄 `dashboard.py`
        > *Code Insight:*
        ```python
        def read_json_file_robust(file_path: Path) -> Dict[str, Any]:
        ```
    📄 `DEPLOY.md`
        > *Code Insight:*
        ```python
        **Multi-Agent as a Service Enterprise Platform - Containerization & CI/CD**
        ```
    📄 `docker-compose.yml`
        > *Code Insight:*
        ```python
        # MAaaS - Multi-Agent as a Service Enterprise Platform
        ```
    📄 `file_doctor.py`
        > *Code Insight:*
        ```python
        def diagnose_file(file_path: Path) -> Tuple[bool, Optional[str], Optional[dict]]:
        ```
    📄 `FILE_DOCTOR_README.md`
        > *Code Insight:*
        ```python
        ```
    📄 `file_utils.py`
        > *Code Insight:*
        ```python
        def read_json_file_robust(file_path: Path) -> Dict[str, Any]:
        ```
    📄 `INTEGRATION_TESTING_GUIDE.md`
        > *Code Insight:*
        ```python
        ### 2. Verify Agent Files
        ```
    📄 `Master Data for MAaaS.pdf`
        [Error reading file: 'utf-8' codec can't decode byte 0xb5 in position 11: invalid start byte]
    📄 `README.md`
        > *Code Insight:*
        ```python
        # MAaaS - Multi-Agent as a Service Enterprise Platform
        ```
    📄 `repair_client_profile.py`
        > *Code Insight:*
        ```python
        def read_json_with_encoding(file_path: Path) -> tuple:
        ```
    📄 `repair_deployment_plan.py`
        > *Code Insight:*
        ```python
        def read_json_with_encoding(file_path: Path) -> dict:
        ```
    📄 `run_swarm_factory.py`
        > *Code Insight:*
        ```python
        Swarm Agency Factory Pipeline
        Prime Orchestrator - Automated Agent Fabrication System
        ```
    📄 `simulate_audit_workflow.py`
        > *Code Insight:*
        ```python
        def simulate_audit_workflow():
        ```
    📄 `specification.md`
        > *Code Insight:*
        ```python
        The Swarm Agency is a **Full-Cycle Multi-Agent as a Service (MAaaS) Enterprise Platform** that transforms client organizations into autonomous, secure, and scalable agentic ecosystems. We operate as the "Meta-Developer," creating and orchestrating specialized AI workforces that handle everything from data management to cybersecurity, reliability engineering, and growth operations.
        ```
    📄 `swarm_protocols.py`
        > *Code Insight:*
        ```python
        Swarm Agency Protocol Initialization
        ```
    📄 `test.py`
        > *Code Insight:*
        ```python
        ```
    📂 **.github/**
        📂 **workflows/**
            📄 `docker-build.yml`
                > *Code Insight:*
                ```python
                ```
    📂 **.venv/**
        📄 `.gitignore`
        📄 `pyvenv.cfg`
        📂 **Include/**
        📂 **Lib/**
            📂 **site-packages/**
                📂 **narwhals/**
                    📄 `compliant.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `dataframe.py`
                        > *Code Insight:*
                        ```python
                        class BaseFrame(Generic[_FrameT]):
                        ```
                    📄 `dependencies.py`
                        > *Code Insight:*
                        ```python
                        def get_polars() -> Any:
                        ```
                    📄 `dtypes.py`
                        > *Code Insight:*
                        ```python
                        def _validate_dtype(dtype: DType | type[DType]) -> None:
                        ```
                    📄 `exceptions.py`
                        > *Code Insight:*
                        ```python
                        class NarwhalsError(ValueError):
                        ```
                    📄 `expr.py`
                        > *Code Insight:*
                        ```python
                        class Expr:
                        def __init__(self, *nodes: ExprNode) -> None:
                        ```
                    📄 `expr_cat.py`
                        > *Code Insight:*
                        ```python
                        class ExprCatNamespace(Generic[ExprT]):
                        def __init__(self, expr: ExprT) -> None:
                        ```
                    📄 `expr_dt.py`
                        > *Code Insight:*
                        ```python
                        class ExprDateTimeNamespace(Generic[ExprT]):
                        def __init__(self, expr: ExprT) -> None:
                        ```
                    📄 `expr_list.py`
                        > *Code Insight:*
                        ```python
                        class ExprListNamespace(Generic[ExprT]):
                        def __init__(self, expr: ExprT) -> None:
                        ```
                    📄 `expr_name.py`
                        > *Code Insight:*
                        ```python
                        class ExprNameNamespace(Generic[ExprT]):
                        def __init__(self, expr: ExprT) -> None:
                        ```
                    📄 `expr_str.py`
                        > *Code Insight:*
                        ```python
                        class ExprStringNamespace(Generic[ExprT]):
                        def __init__(self, expr: ExprT) -> None:
                        ```
                    📄 `expr_struct.py`
                        > *Code Insight:*
                        ```python
                        class ExprStructNamespace(Generic[ExprT]):
                        def __init__(self, expr: ExprT) -> None:
                        ```
                    📄 `functions.py`
                        > *Code Insight:*
                        ```python
                        def concat(items: Iterable[FrameT], *, how: ConcatMethod = "vertical") -> FrameT:
                        ```
                    📄 `group_by.py`
                        > *Code Insight:*
                        ```python
                        class GroupBy(Generic[DataFrameT]):
                        def __init__(
                        ```
                    📄 `plugins.py`
                        > *Code Insight:*
                        ```python
                        def _discover_entrypoints() -> EntryPoints:
                        ```
                    📄 `py.typed`
                    📄 `schema.py`
                        > *Code Insight:*
                        ```python
                        class Schema(OrderedDict[str, "DType"]):
                        ```
                    📄 `selectors.py`
                        > *Code Insight:*
                        ```python
                        class Selector(Expr):
                        def _to_expr(self) -> Expr:
                        ```
                    📄 `series.py`
                        > *Code Insight:*
                        ```python
                        class Series(Generic[IntoSeriesT]):
                        ```
                    📄 `series_cat.py`
                        > *Code Insight:*
                        ```python
                        class SeriesCatNamespace(Generic[SeriesT]):
                        def __init__(self, series: SeriesT) -> None:
                        ```
                    📄 `series_dt.py`
                        > *Code Insight:*
                        ```python
                        class SeriesDateTimeNamespace(Generic[SeriesT]):
                        def __init__(self, series: SeriesT) -> None:
                        ```
                    📄 `series_list.py`
                        > *Code Insight:*
                        ```python
                        class SeriesListNamespace(Generic[SeriesT]):
                        def __init__(self, series: SeriesT) -> None:
                        ```
                    📄 `series_str.py`
                        > *Code Insight:*
                        ```python
                        class SeriesStringNamespace(Generic[SeriesT]):
                        def __init__(self, series: SeriesT) -> None:
                        ```
                    📄 `series_struct.py`
                        > *Code Insight:*
                        ```python
                        class SeriesStructNamespace(Generic[SeriesT]):
                        def __init__(self, series: SeriesT) -> None:
                        ```
                    📄 `this.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `translate.py`
                        > *Code Insight:*
                        ```python
                        def to_native(
                        def to_native(
                        def to_native(
                        def to_native(narwhals_object: Any, *, pass_through: bool) -> Any: ...
                        ```
                    📄 `typing.py`
                        > *Code Insight:*
                        ```python
                        class SupportsNativeNamespace(Protocol):
                        def __native_namespace__(self) -> ModuleType: ...
                        ```
                    📄 `utils.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `_constants.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `_duration.py`
                        > *Code Insight:*
                        ```python
                        class Interval:
                        def __init__(self, multiple: int, unit: IntervalUnit, /) -> None:
                        ```
                    📄 `_enum.py`
                        > *Code Insight:*
                        ```python
                        class NoAutoEnum(Enum):
                        ```
                    📄 `_exceptions.py`
                        > *Code Insight:*
                        ```python
                        def find_stacklevel() -> int:
                        ```
                    📄 `_expression_parsing.py`
                        > *Code Insight:*
                        ```python
                        def is_expr(obj: Any) -> TypeIs[Expr]:
                        ```
                    📄 `_namespace.py`
                        > *Code Insight:*
                        ```python
                        class Namespace(Generic[CompliantNamespaceT_co]):
                        ```
                    📄 `_native.py`
                        > *Code Insight:*
                        ```python
                        def wrapping_in_df(native: IntoDataFrameT) -> DataFrame[IntoDataFrameT]: ...
                        def wrapping_in_lf(native: IntoLazyFrameT) -> LazyFrame[IntoLazyFrameT]: ...
                        def wrapping_in_ser(native: IntoSeriesT) -> Series[IntoSeriesT]: ...
                        ```
                    📄 `_translate.py`
                        > *Code Insight:*
                        ```python
                        class ToOther(Protocol[ToOtherT_co]):
                        def to_other(self, *args: Any, **kwds: Any) -> ToOtherT_co: ...
                        ```
                    📄 `_typing.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `_typing_compat.py`
                        > *Code Insight:*
                        ```python
                        def TypeVar(
                        ```
                    📄 `_utils.py`
                        > *Code Insight:*
                        ```python
                        class _SupportsVersion(Protocol):
                        ```
                    📄 `__init__.py`
                        > *Code Insight:*
                        ```python
                        def __getattr__(name: str) -> _t.Any:
                        ```
                    📂 **stable/**
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📂 **v1/**
                            📄 `dependencies.py`
                                > *Code Insight:*
                                ```python
                                def is_pandas_dataframe(df: Any) -> TypeIs[pd.DataFrame]:
                                ```
                            📄 `dtypes.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `selectors.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `typing.py`
                                > *Code Insight:*
                                ```python
                                class DataFrameLike(Protocol):
                                def __dataframe__(self, *args: Any, **kwargs: Any) -> Any: ...
                                ```
                            📄 `_dtypes.py`
                                > *Code Insight:*
                                ```python
                                class Datetime(NwDatetime):
                                def __init__(
                                ```
                            📄 `_namespace.py`
                                > *Code Insight:*
                                ```python
                                class Namespace(NwNamespace[CompliantNamespaceT_co], version=Version.V1): ...
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                class DataFrame(NwDataFrame[IntoDataFrameT]):  # type: ignore[type-var]
                                ```
                        📂 **v2/**
                            📄 `dependencies.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `dtypes.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `selectors.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `typing.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `_namespace.py`
                                > *Code Insight:*
                                ```python
                                class Namespace(NwNamespace[CompliantNamespaceT_co], version=Version.V2): ...
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                class DataFrame(NwDataFrame[IntoDataFrameT]):
                                ```
                    📂 **testing/**
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📂 **asserts/**
                            📄 `series.py`
                                > *Code Insight:*
                                ```python
                                def assert_series_equal(
                                ```
                            📄 `utils.py`
                                > *Code Insight:*
                                ```python
                                def raise_assertion_error(
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                    📂 **_arrow/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class ArrowDataFrame(
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            class ArrowExpr(EagerExpr["ArrowDataFrame", ArrowSeries]):
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            class ArrowGroupBy(EagerGroupBy["ArrowDataFrame", "ArrowExpr", "Aggregation"]):
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class ArrowNamespace(
                            ```
                        📄 `selectors.py`
                            > *Code Insight:*
                            ```python
                            class ArrowSelectorNamespace(EagerSelectorNamespace["ArrowDataFrame", "ArrowSeries"]):
                            def _selector(self) -> type[ArrowSelector]:
                            ```
                        📄 `series.py`
                            > *Code Insight:*
                            ```python
                            def maybe_extract_py_scalar(
                            ```
                        📄 `series_cat.py`
                            > *Code Insight:*
                            ```python
                            class ArrowSeriesCatNamespace(ArrowSeriesNamespace, CatNamespace["ArrowSeries"]):
                            def get_categories(self) -> ArrowSeries:
                            ```
                        📄 `series_dt.py`
                            > *Code Insight:*
                            ```python
                            class ArrowSeriesDateTimeNamespace(
                            ```
                        📄 `series_list.py`
                            > *Code Insight:*
                            ```python
                            class ArrowSeriesListNamespace(ArrowSeriesNamespace, ListNamespace["ArrowSeries"]):
                            def len(self) -> ArrowSeries:
                            ```
                        📄 `series_str.py`
                            > *Code Insight:*
                            ```python
                            class ArrowSeriesStringNamespace(ArrowSeriesNamespace, StringNamespace["ArrowSeries"]):
                            def len_chars(self) -> ArrowSeries:
                            ```
                        📄 `series_struct.py`
                            > *Code Insight:*
                            ```python
                            class ArrowSeriesStructNamespace(ArrowSeriesNamespace, StructNamespace["ArrowSeries"]):
                            def field(self, name: str) -> ArrowSeries:
                            ```
                        📄 `typing.py`
                            > *Code Insight:*
                            ```python
                            class _BasicDataType(pa.DataType, Generic[_AsPyType]): ...
                            ```
                        📄 `utils.py`
                            > *Code Insight:*
                            ```python
                            def is_timestamp(t: Any) -> TypeIs[pa.TimestampType[Any, Any]]: ...
                            def is_duration(t: Any) -> TypeIs[pa.DurationType[Any]]: ...
                            def is_list(t: Any) -> TypeIs[pa.ListType[Any]]: ...
                            def is_large_list(t: Any) -> TypeIs[pa.LargeListType[Any]]: ...
                            def is_fixed_size_list(t: Any) -> TypeIs[pa.FixedSizeListType[Any, Any]]: ...
                            def is_dictionary(t: Any) -> TypeIs[pa.DictionaryType[Any, Any, Any]]: ...
                            def extract_regex(
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_compliant/**
                        📄 `any_namespace.py`
                            > *Code Insight:*
                            ```python
                            class NamespaceAccessor(_StoresCompliant[CompliantT_co], Protocol[CompliantT_co]):
                            ```
                        📄 `column.py`
                            > *Code Insight:*
                            ```python
                            class CompliantColumn(Protocol):
                            ```
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class CompliantFrame(
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            class NativeExpr(Protocol):
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            def _evaluate_aliases(
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class CompliantNamespace(Protocol[CompliantFrameT, CompliantExprT]):
                            ```
                        📄 `selectors.py`
                            > *Code Insight:*
                            ```python
                            class CompliantSelectorNamespace(Protocol[FrameT, SeriesOrExprT]):
                            ```
                        📄 `series.py`
                            > *Code Insight:*
                            ```python
                            class HistData(TypedDict, Generic[NativeSeriesT, "_CountsT_co"]):
                            ```
                        📄 `typing.py`
                            > *Code Insight:*
                            ```python
                            class ScalarKwargs(TypedDict, total=False):
                            ```
                        📄 `window.py`
                            > *Code Insight:*
                            ```python
                            class WindowInputs(Generic[NativeExprT_co]):
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_dask/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class DaskLazyFrame(
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            def simple_aggregation(attr: str) -> Any:
                            ```
                        📄 `expr_dt.py`
                            > *Code Insight:*
                            ```python
                            class DaskExprDateTimeNamespace(
                            def date(self) -> DaskExpr:
                            ```
                        📄 `expr_str.py`
                            > *Code Insight:*
                            ```python
                            class DaskExprStringNamespace(LazyExprNamespace["DaskExpr"], StringNamespace["DaskExpr"]):
                            def len_chars(self) -> DaskExpr:
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            def n_unique() -> dd.Aggregation:
                            def chunk(s: PandasSeriesGroupBy) -> pd.Series[Any]:
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class DaskNamespace(
                            ```
                        📄 `selectors.py`
                            > *Code Insight:*
                            ```python
                            class DaskSelectorNamespace(LazySelectorNamespace["DaskLazyFrame", "dx.Series"]):  # pyright: ignore[reportInvalidTypeArguments]
                            def _selector(self) -> type[DaskSelector]:
                            ```
                        📄 `utils.py`
                            > *Code Insight:*
                            ```python
                            def evaluate_exprs(df: DaskLazyFrame, /, *exprs: DaskExpr) -> list[tuple[str, dx.Series]]:
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_duckdb/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBLazyFrame(
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBExpr(SQLExpr["DuckDBLazyFrame", "Expression"]):
                            ```
                        📄 `expr_dt.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBExprDateTimeNamespace(SQLExprDateTimeNamesSpace["DuckDBExpr"]):
                            def millisecond(self) -> DuckDBExpr:
                            ```
                        📄 `expr_list.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBExprListNamespace(
                            def len(self) -> DuckDBExpr:
                            ```
                        📄 `expr_str.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBExprStringNamespace(SQLExprStringNamespace["DuckDBExpr"]):
                            def to_datetime(self, format: str | None) -> DuckDBExpr:
                            ```
                        📄 `expr_struct.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBExprStructNamespace(
                            def field(self, name: str) -> DuckDBExpr:
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBGroupBy(SQLGroupBy["DuckDBLazyFrame", "DuckDBExpr", "Expression"]):
                            def __init__(
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBNamespace(
                            ```
                        📄 `selectors.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBSelectorNamespace(LazySelectorNamespace["DuckDBLazyFrame", "Expression"]):
                            def _selector(self) -> type[DuckDBSelector]:
                            ```
                        📄 `series.py`
                            > *Code Insight:*
                            ```python
                            class DuckDBInterchangeSeries:
                            def __init__(self, df: duckdb.DuckDBPyRelation, version: Version) -> None:
                            ```
                        📄 `typing.py`
                            > *Code Insight:*
                            ```python
                            class WindowExpressionKwargs(TypedDict, total=False):
                            ```
                        📄 `utils.py`
                            > *Code Insight:*
                            ```python
                            def lambda_expr(
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_ibis/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class IbisLazyFrame(
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            class IbisExpr(SQLExpr["IbisLazyFrame", "ir.Value"]):
                            ```
                        📄 `expr_dt.py`
                            > *Code Insight:*
                            ```python
                            class IbisExprDateTimeNamespace(SQLExprDateTimeNamesSpace["IbisExpr"]):
                            def millisecond(self) -> IbisExpr:
                            ```
                        📄 `expr_list.py`
                            > *Code Insight:*
                            ```python
                            class IbisExprListNamespace(LazyExprNamespace["IbisExpr"], ListNamespace["IbisExpr"]):
                            def len(self) -> IbisExpr:
                            ```
                        📄 `expr_str.py`
                            > *Code Insight:*
                            ```python
                            class IbisExprStringNamespace(SQLExprStringNamespace["IbisExpr"]):
                            def strip_chars(self, characters: str | None) -> IbisExpr:
                            ```
                        📄 `expr_struct.py`
                            > *Code Insight:*
                            ```python
                            class IbisExprStructNamespace(LazyExprNamespace["IbisExpr"], StructNamespace["IbisExpr"]):
                            def field(self, name: str) -> IbisExpr:
                            def func(expr: ir.StructColumn) -> ir.Column:
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            class IbisGroupBy(SQLGroupBy["IbisLazyFrame", "IbisExpr", "ir.Value"]):
                            def __init__(
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class IbisNamespace(SQLNamespace[IbisLazyFrame, IbisExpr, "ir.Table", "ir.Value"]):
                            ```
                        📄 `selectors.py`
                            > *Code Insight:*
                            ```python
                            class IbisSelectorNamespace(LazySelectorNamespace["IbisLazyFrame", "ir.Value"]):
                            def _selector(self) -> type[IbisSelector]:
                            ```
                        📄 `series.py`
                            > *Code Insight:*
                            ```python
                            class IbisInterchangeSeries:
                            def __init__(self, df: Any, version: Version) -> None:
                            ```
                        📄 `utils.py`
                            > *Code Insight:*
                            ```python
                            def lit(value: bool, dtype: None = ...) -> ir.BooleanScalar: ...  # noqa: FBT001
                            def lit(value: int, dtype: None = ...) -> ir.IntegerScalar: ...
                            def lit(value: float, dtype: None = ...) -> ir.FloatingScalar: ...
                            def lit(value: str, dtype: None = ...) -> ir.StringScalar: ...
                            def lit(value: PythonLiteral | ir.Value, dtype: None = ...) -> ir.Scalar: ...
                            def lit(value: Any, dtype: Any) -> Incomplete: ...
                            def lit(value: Any, dtype: Any | None = None) -> Incomplete:
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_interchange/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class DtypeKind(enum.IntEnum):
                            ```
                        📄 `series.py`
                            > *Code Insight:*
                            ```python
                            class InterchangeSeries:
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_pandas_like/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class PandasLikeDataFrame(
                            def __init__(
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            def window_kwargs_to_pandas_equivalent(  # noqa: C901
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            def _native_agg(name: NativeAggregation, /, **kwds: Unpack[ScalarKwargs]) -> _NativeAgg:
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class PandasLikeNamespace(
                            def _dataframe(self) -> type[PandasLikeDataFrame]:
                            ```
                        📄 `selectors.py`
                            > *Code Insight:*
                            ```python
                            class PandasSelectorNamespace(
                            def _selector(self) -> type[PandasSelector]:
                            ```
                        📄 `series.py`
                            > *Code Insight:*
                            ```python
                            class PandasLikeSeries(EagerSeries[Any]):
                            def __init__(
                            ```
                        📄 `series_cat.py`
                            > *Code Insight:*
                            ```python
                            class PandasLikeSeriesCatNamespace(
                            def get_categories(self) -> PandasLikeSeries:
                            ```
                        📄 `series_dt.py`
                            > *Code Insight:*
                            ```python
                            class PandasLikeSeriesDateTimeNamespace(
                            def date(self) -> PandasLikeSeries:
                            ```
                        📄 `series_list.py`
                            > *Code Insight:*
                            ```python
                            class PandasLikeSeriesListNamespace(
                            def len(self) -> PandasLikeSeries:
                            ```
                        📄 `series_str.py`
                            > *Code Insight:*
                            ```python
                            class PandasLikeSeriesStringNamespace(
                            def len_chars(self) -> PandasLikeSeries:
                            ```
                        📄 `series_struct.py`
                            > *Code Insight:*
                            ```python
                            class PandasLikeSeriesStructNamespace(
                            def field(self, name: str) -> PandasLikeSeries:
                            ```
                        📄 `typing.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `utils.py`
                            > *Code Insight:*
                            ```python
                            def is_pandas_or_modin(implementation: Implementation) -> bool:
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_polars/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class PolarsBaseFrame(Generic[NativePolarsFrame]):
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            class PolarsExpr:
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            class PolarsGroupBy:
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class PolarsNamespace:
                            ```
                        📄 `series.py`
                            > *Code Insight:*
                            ```python
                            class PolarsSeries:
                            ```
                        📄 `typing.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `utils.py`
                            > *Code Insight:*
                            ```python
                            def extract_native(obj: _StoresNative[NativeT]) -> NativeT: ...
                            def extract_native(obj: T) -> T: ...
                            def extract_native(obj: _StoresNative[NativeT] | T) -> NativeT | T:
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_spark_like/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeLazyFrame(
                            def __init__(
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeExpr(SQLExpr["SparkLikeLazyFrame", "Column"]):
                            def __init__(
                            ```
                        📄 `expr_dt.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeExprDateTimeNamespace(SQLExprDateTimeNamesSpace["SparkLikeExpr"]):
                            def _weekday(self, expr: Column) -> Column:
                            ```
                        📄 `expr_list.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeExprListNamespace(
                            def len(self) -> SparkLikeExpr:
                            ```
                        📄 `expr_str.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeExprStringNamespace(SQLExprStringNamespace["SparkLikeExpr"]):
                            def to_datetime(self, format: str | None) -> SparkLikeExpr:
                            ```
                        📄 `expr_struct.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeExprStructNamespace(
                            def field(self, name: str) -> SparkLikeExpr:
                            def func(expr: Column) -> Column:
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeLazyGroupBy(SQLGroupBy["SparkLikeLazyFrame", "SparkLikeExpr", "Column"]):
                            def __init__(
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeNamespace(
                            def __init__(self, *, version: Version, implementation: Implementation) -> None:
                            ```
                        📄 `selectors.py`
                            > *Code Insight:*
                            ```python
                            class SparkLikeSelectorNamespace(LazySelectorNamespace["SparkLikeLazyFrame", "Column"]):
                            def _selector(self) -> type[SparkLikeSelector]:
                            ```
                        📄 `utils.py`
                            > *Code Insight:*
                            ```python
                            def native_to_narwhals_dtype(  # noqa: C901, PLR0912
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **_sql/**
                        📄 `dataframe.py`
                            > *Code Insight:*
                            ```python
                            class SQLLazyFrame(
                            def _evaluate_window_expr(
                            ```
                        📄 `expr.py`
                            > *Code Insight:*
                            ```python
                            class SQLExpr(LazyExpr[SQLLazyFrameT, NativeExprT], Protocol[SQLLazyFrameT, NativeExprT]):
                            ```
                        📄 `expr_dt.py`
                            > *Code Insight:*
                            ```python
                            class SQLExprDateTimeNamesSpace(
                            def _function(self, name: str, *args: Any) -> NativeExpr:
                            ```
                        📄 `expr_str.py`
                            > *Code Insight:*
                            ```python
                            class SQLExprStringNamespace(
                            def _lit(self, value: Any) -> NativeExpr:
                            ```
                        📄 `group_by.py`
                            > *Code Insight:*
                            ```python
                            class SQLGroupBy(
                            ```
                        📄 `namespace.py`
                            > *Code Insight:*
                            ```python
                            class SQLNamespace(
                            def _function(self, name: str, *args: NativeExprT | PythonLiteral) -> NativeExprT: ...
                            def _lit(self, value: Any) -> NativeExprT: ...
                            def _when(
                            def _coalesce(self, *exprs: NativeExprT) -> NativeExprT: ...
                            ```
                        📄 `typing.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                📂 **narwhals-2.14.0.dist-info/**
                    📄 `INSTALLER`
                    📄 `METADATA`
                    📄 `RECORD`
                    📄 `WHEEL`
                    📂 **licenses/**
                        📄 `LICENSE.md`
                            > *Code Insight:*
                            ```python
                            ```
                📂 **packaging/**
                    📄 `markers.py`
                        > *Code Insight:*
                        ```python
                        class InvalidMarker(ValueError):
                        ```
                    📄 `metadata.py`
                        > *Code Insight:*
                        ```python
                        class ExceptionGroup(Exception):
                        ```
                    📄 `py.typed`
                    📄 `requirements.py`
                        > *Code Insight:*
                        ```python
                        class InvalidRequirement(ValueError):
                        ```
                    📄 `specifiers.py`
                        > *Code Insight:*
                        ```python
                        def _coerce_version(version: UnparsedVersion) -> Version:
                        ```
                    📄 `tags.py`
                        > *Code Insight:*
                        ```python
                        class Tag:
                        ```
                    📄 `utils.py`
                        > *Code Insight:*
                        ```python
                        class InvalidName(ValueError):
                        ```
                    📄 `version.py`
                        > *Code Insight:*
                        ```python
                        class _Version(NamedTuple):
                        ```
                    📄 `_elffile.py`
                        > *Code Insight:*
                        ```python
                        class ELFInvalid(ValueError):
                        ```
                    📄 `_manylinux.py`
                        > *Code Insight:*
                        ```python
                        def _parse_elf(path: str) -> Generator[ELFFile | None, None, None]:
                        ```
                    📄 `_musllinux.py`
                        > *Code Insight:*
                        ```python
                        class _MuslVersion(NamedTuple):
                        ```
                    📄 `_parser.py`
                        > *Code Insight:*
                        ```python
                        class Node:
                        def __init__(self, value: str) -> None:
                        ```
                    📄 `_structures.py`
                        > *Code Insight:*
                        ```python
                        class InfinityType:
                        def __repr__(self) -> str:
                        ```
                    📄 `_tokenizer.py`
                        > *Code Insight:*
                        ```python
                        class Token:
                        ```
                    📄 `__init__.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📂 **licenses/**
                        📄 `_spdx.py`
                            > *Code Insight:*
                            ```python
                            class SPDXLicense(TypedDict):
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            class InvalidLicenseExpression(ValueError):
                            ```
                📂 **packaging-25.0.dist-info/**
                    📄 `INSTALLER`
                    📄 `METADATA`
                    📄 `RECORD`
                    📄 `WHEEL`
                    📂 **licenses/**
                        📄 `LICENSE`
                        📄 `LICENSE.APACHE`
                        📄 `LICENSE.BSD`
                📂 **pip/**
                    📄 `py.typed`
                    📄 `__init__.py`
                        > *Code Insight:*
                        ```python
                        def main(args: list[str] | None = None) -> int:
                        ```
                    📄 `__main__.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `__pip-runner__.py`
                        > *Code Insight:*
                        ```python
                        def version_str(version):  # type: ignore
                        ```
                    📂 **_internal/**
                        📄 `build_env.py`
                            > *Code Insight:*
                            ```python
                            class ExtraEnviron(TypedDict, total=False):
                            ```
                        📄 `cache.py`
                            > *Code Insight:*
                            ```python
                            def _hash_dict(d: dict[str, str]) -> str:
                            ```
                        📄 `configuration.py`
                            > *Code Insight:*
                            ```python
                            def _normalize_name(name: str) -> str:
                            ```
                        📄 `exceptions.py`
                            > *Code Insight:*
                            ```python
                            def _is_kebab_case(s: str) -> bool:
                            ```
                        📄 `main.py`
                            > *Code Insight:*
                            ```python
                            def main(args: list[str] | None = None) -> int:
                            ```
                        📄 `pyproject.py`
                            > *Code Insight:*
                            ```python
                            def _is_list_of_str(obj: Any) -> bool:
                            ```
                        📄 `self_outdated_check.py`
                            > *Code Insight:*
                            ```python
                            def _get_statefile_name(key: str) -> str:
                            ```
                        📄 `wheel_builder.py`
                            > *Code Insight:*
                            ```python
                            def _contains_egg_info(s: str) -> bool:
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            def main(args: list[str] | None = None) -> int:
                            ```
                        📂 **cli/**
                            📄 `autocompletion.py`
                                > *Code Insight:*
                                ```python
                                def autocomplete() -> None:
                                ```
                            📄 `base_command.py`
                                > *Code Insight:*
                                ```python
                                class Command(CommandContextMixIn):
                                ```
                            📄 `cmdoptions.py`
                                > *Code Insight:*
                                ```python
                                def raise_option_error(parser: OptionParser, option: Option, msg: str) -> None:
                                ```
                            📄 `command_context.py`
                                > *Code Insight:*
                                ```python
                                class CommandContextMixIn:
                                def __init__(self) -> None:
                                ```
                            📄 `index_command.py`
                                > *Code Insight:*
                                ```python
                                def _create_truststore_ssl_context() -> SSLContext | None:
                                ```
                            📄 `main.py`
                                > *Code Insight:*
                                ```python
                                def main(args: list[str] | None = None) -> int:
                                ```
                            📄 `main_parser.py`
                                > *Code Insight:*
                                ```python
                                def create_main_parser() -> ConfigOptionParser:
                                ```
                            📄 `parser.py`
                                > *Code Insight:*
                                ```python
                                class PrettyHelpFormatter(optparse.IndentedHelpFormatter):
                                ```
                            📄 `progress_bars.py`
                                > *Code Insight:*
                                ```python
                                def _rich_download_progress_bar(
                                ```
                            📄 `req_command.py`
                                > *Code Insight:*
                                ```python
                                def should_ignore_regular_constraints(options: Values) -> bool:
                                ```
                            📄 `spinners.py`
                                > *Code Insight:*
                                ```python
                                class SpinnerInterface:
                                def spin(self) -> None:
                                ```
                            📄 `status_codes.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **commands/**
                            📄 `cache.py`
                                > *Code Insight:*
                                ```python
                                class CacheCommand(Command):
                                ```
                            📄 `check.py`
                                > *Code Insight:*
                                ```python
                                class CheckCommand(Command):
                                ```
                            📄 `completion.py`
                                > *Code Insight:*
                                ```python
                                class CompletionCommand(Command):
                                ```
                            📄 `configuration.py`
                                > *Code Insight:*
                                ```python
                                class ConfigurationCommand(Command):
                                ```
                            📄 `debug.py`
                                > *Code Insight:*
                                ```python
                                def show_value(name: str, value: Any) -> None:
                                ```
                            📄 `download.py`
                                > *Code Insight:*
                                ```python
                                class DownloadCommand(RequirementCommand):
                                ```
                            📄 `freeze.py`
                                > *Code Insight:*
                                ```python
                                def _should_suppress_build_backends() -> bool:
                                ```
                            📄 `hash.py`
                                > *Code Insight:*
                                ```python
                                class HashCommand(Command):
                                ```
                            📄 `help.py`
                                > *Code Insight:*
                                ```python
                                class HelpCommand(Command):
                                ```
                            📄 `index.py`
                                > *Code Insight:*
                                ```python
                                class IndexCommand(IndexGroupCommand):
                                ```
                            📄 `inspect.py`
                                > *Code Insight:*
                                ```python
                                class InspectCommand(Command):
                                ```
                            📄 `install.py`
                                > *Code Insight:*
                                ```python
                                class InstallCommand(RequirementCommand):
                                ```
                            📄 `list.py`
                                > *Code Insight:*
                                ```python
                                class _DistWithLatestInfo(BaseDistribution):
                                ```
                            📄 `lock.py`
                                > *Code Insight:*
                                ```python
                                class LockCommand(RequirementCommand):
                                ```
                            📄 `search.py`
                                > *Code Insight:*
                                ```python
                                class TransformedHit(TypedDict):
                                ```
                            📄 `show.py`
                                > *Code Insight:*
                                ```python
                                def normalize_project_url_label(label: str) -> str:
                                ```
                            📄 `uninstall.py`
                                > *Code Insight:*
                                ```python
                                class UninstallCommand(Command, SessionCommandMixin):
                                ```
                            📄 `wheel.py`
                                > *Code Insight:*
                                ```python
                                class WheelCommand(RequirementCommand):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def create_command(name: str, **kwargs: Any) -> Command:
                                ```
                        📂 **distributions/**
                            📄 `base.py`
                                > *Code Insight:*
                                ```python
                                class AbstractDistribution(metaclass=abc.ABCMeta):
                                ```
                            📄 `installed.py`
                                > *Code Insight:*
                                ```python
                                class InstalledDistribution(AbstractDistribution):
                                ```
                            📄 `sdist.py`
                                > *Code Insight:*
                                ```python
                                class SourceDistribution(AbstractDistribution):
                                ```
                            📄 `wheel.py`
                                > *Code Insight:*
                                ```python
                                class WheelDistribution(AbstractDistribution):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def make_distribution_for_install_requirement(
                                ```
                        📂 **index/**
                            📄 `collector.py`
                                > *Code Insight:*
                                ```python
                                def _match_vcs_scheme(url: str) -> str | None:
                                ```
                            📄 `package_finder.py`
                                > *Code Insight:*
                                ```python
                                def _check_link_requires_python(
                                ```
                            📄 `sources.py`
                                > *Code Insight:*
                                ```python
                                class LinkSource:
                                def link(self) -> Link | None:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **locations/**
                            📄 `base.py`
                                > *Code Insight:*
                                ```python
                                def get_major_minor_version() -> str:
                                ```
                            📄 `_distutils.py`
                                > *Code Insight:*
                                ```python
                                def distutils_scheme(
                                ```
                            📄 `_sysconfig.py`
                                > *Code Insight:*
                                ```python
                                def _should_use_osx_framework_prefix() -> bool:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def _should_use_sysconfig() -> bool:
                                ```
                        📂 **metadata/**
                            📄 `base.py`
                                > *Code Insight:*
                                ```python
                                class BaseEntryPoint(Protocol):
                                def name(self) -> str:
                                ```
                            📄 `pkg_resources.py`
                                > *Code Insight:*
                                ```python
                                class EntryPoint(NamedTuple):
                                ```
                            📄 `_json.py`
                                > *Code Insight:*
                                ```python
                                def json_name(field: str) -> str:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def _should_use_importlib_metadata() -> bool:
                                ```
                            📂 **importlib/**
                                📄 `_compat.py`
                                    > *Code Insight:*
                                    ```python
                                    class BadMetadata(ValueError):
                                    def __init__(self, dist: importlib.metadata.Distribution, *, reason: str) -> None:
                                    ```
                                📄 `_dists.py`
                                    > *Code Insight:*
                                    ```python
                                    class WheelDistribution(importlib.metadata.Distribution):
                                    ```
                                📄 `_envs.py`
                                    > *Code Insight:*
                                    ```python
                                    def _looks_like_wheel(location: str) -> bool:
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **models/**
                            📄 `candidate.py`
                                > *Code Insight:*
                                ```python
                                class InstallationCandidate:
                                ```
                            📄 `direct_url.py`
                                > *Code Insight:*
                                ```python
                                class DirectUrlValidationError(Exception):
                                ```
                            📄 `format_control.py`
                                > *Code Insight:*
                                ```python
                                class FormatControl:
                                ```
                            📄 `index.py`
                                > *Code Insight:*
                                ```python
                                class PackageIndex:
                                ```
                            📄 `installation_report.py`
                                > *Code Insight:*
                                ```python
                                class InstallationReport:
                                def __init__(self, install_requirements: Sequence[InstallRequirement]):
                                ```
                            📄 `link.py`
                                > *Code Insight:*
                                ```python
                                class LinkHash:
                                ```
                            📄 `pylock.py`
                                > *Code Insight:*
                                ```python
                                def is_valid_pylock_file_name(path: Path) -> bool:
                                ```
                            📄 `scheme.py`
                                > *Code Insight:*
                                ```python
                                class Scheme:
                                ```
                            📄 `search_scope.py`
                                > *Code Insight:*
                                ```python
                                class SearchScope:
                                ```
                            📄 `selection_prefs.py`
                                > *Code Insight:*
                                ```python
                                class SelectionPreferences:
                                ```
                            📄 `target_python.py`
                                > *Code Insight:*
                                ```python
                                class TargetPython:
                                ```
                            📄 `wheel.py`
                                > *Code Insight:*
                                ```python
                                class Wheel:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **network/**
                            📄 `auth.py`
                                > *Code Insight:*
                                ```python
                                class Credentials(NamedTuple):
                                ```
                            📄 `cache.py`
                                > *Code Insight:*
                                ```python
                                def is_from_cache(response: Response) -> bool:
                                ```
                            📄 `download.py`
                                > *Code Insight:*
                                ```python
                                def _get_http_response_size(resp: Response) -> int | None:
                                ```
                            📄 `lazy_wheel.py`
                                > *Code Insight:*
                                ```python
                                class HTTPRangeRequestUnsupported(Exception):
                                ```
                            📄 `session.py`
                                > *Code Insight:*
                                ```python
                                def looks_like_ci() -> bool:
                                ```
                            📄 `utils.py`
                                > *Code Insight:*
                                ```python
                                def raise_for_status(resp: Response) -> None:
                                ```
                            📄 `xmlrpc.py`
                                > *Code Insight:*
                                ```python
                                class PipXmlrpcTransport(xmlrpc.client.Transport):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **operations/**
                            📄 `check.py`
                                > *Code Insight:*
                                ```python
                                class PackageDetails(NamedTuple):
                                ```
                            📄 `freeze.py`
                                > *Code Insight:*
                                ```python
                                class _EditableInfo(NamedTuple):
                                ```
                            📄 `prepare.py`
                                > *Code Insight:*
                                ```python
                                def _get_prepared_distribution(
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **build/**
                                📄 `build_tracker.py`
                                    > *Code Insight:*
                                    ```python
                                    def update_env_context_manager(**changes: str) -> Generator[None, None, None]:
                                    ```
                                📄 `metadata.py`
                                    > *Code Insight:*
                                    ```python
                                    def generate_metadata(
                                    ```
                                📄 `metadata_editable.py`
                                    > *Code Insight:*
                                    ```python
                                    def generate_editable_metadata(
                                    ```
                                📄 `wheel.py`
                                    > *Code Insight:*
                                    ```python
                                    def build_wheel_pep517(
                                    ```
                                📄 `wheel_editable.py`
                                    > *Code Insight:*
                                    ```python
                                    def build_wheel_editable(
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **install/**
                                📄 `wheel.py`
                                    > *Code Insight:*
                                    ```python
                                    class File(Protocol):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **req/**
                            📄 `constructors.py`
                                > *Code Insight:*
                                ```python
                                def _strip_extras(path: str) -> tuple[str, str | None]:
                                ```
                            📄 `req_dependency_group.py`
                                > *Code Insight:*
                                ```python
                                def parse_dependency_groups(groups: list[tuple[str, str]]) -> list[str]:
                                ```
                            📄 `req_file.py`
                                > *Code Insight:*
                                ```python
                                class ParsedRequirement:
                                ```
                            📄 `req_install.py`
                                > *Code Insight:*
                                ```python
                                class InstallRequirement:
                                ```
                            📄 `req_set.py`
                                > *Code Insight:*
                                ```python
                                class RequirementSet:
                                def __init__(self, check_supported_wheels: bool = True) -> None:
                                ```
                            📄 `req_uninstall.py`
                                > *Code Insight:*
                                ```python
                                def _script_names(
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                class InstallationResult:
                                ```
                        📂 **resolution/**
                            📄 `base.py`
                                > *Code Insight:*
                                ```python
                                class BaseResolver:
                                def resolve(
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **legacy/**
                                📄 `resolver.py`
                                    > *Code Insight:*
                                    ```python
                                    def _check_dist_requires_python(
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **resolvelib/**
                                📄 `base.py`
                                    > *Code Insight:*
                                    ```python
                                    def format_name(project: NormalizedName, extras: frozenset[NormalizedName]) -> str:
                                    ```
                                📄 `candidates.py`
                                    > *Code Insight:*
                                    ```python
                                    def as_base_candidate(candidate: Candidate) -> BaseCandidate | None:
                                    ```
                                📄 `factory.py`
                                    > *Code Insight:*
                                    ```python
                                    class ConflictCause(Protocol):
                                    ```
                                📄 `found_candidates.py`
                                    > *Code Insight:*
                                    ```python
                                    def _iter_built(infos: Iterator[IndexCandidateInfo]) -> Iterator[Candidate]:
                                    ```
                                📄 `provider.py`
                                    > *Code Insight:*
                                    ```python
                                    def _get_with_identifier(
                                    ```
                                📄 `reporter.py`
                                    > *Code Insight:*
                                    ```python
                                    class PipReporter(BaseReporter[Requirement, Candidate, str]):
                                    def __init__(self, constraints: Mapping[str, Constraint] | None = None) -> None:
                                    ```
                                📄 `requirements.py`
                                    > *Code Insight:*
                                    ```python
                                    class ExplicitRequirement(Requirement):
                                    def __init__(self, candidate: Candidate) -> None:
                                    ```
                                📄 `resolver.py`
                                    > *Code Insight:*
                                    ```python
                                    class Resolver(BaseResolver):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **utils/**
                            📄 `appdirs.py`
                                > *Code Insight:*
                                ```python
                                def user_cache_dir(appname: str) -> str:
                                ```
                            📄 `compat.py`
                                > *Code Insight:*
                                ```python
                                def has_tls() -> bool:
                                ```
                            📄 `compatibility_tags.py`
                                > *Code Insight:*
                                ```python
                                def version_info_to_nodot(version_info: tuple[int, ...]) -> str:
                                ```
                            📄 `datetime.py`
                                > *Code Insight:*
                                ```python
                                def today_is_later_than(year: int, month: int, day: int) -> bool:
                                ```
                            📄 `deprecation.py`
                                > *Code Insight:*
                                ```python
                                class PipDeprecationWarning(Warning):
                                ```
                            📄 `direct_url_helpers.py`
                                > *Code Insight:*
                                ```python
                                def direct_url_as_pep440_direct_reference(direct_url: DirectUrl, name: str) -> str:
                                ```
                            📄 `egg_link.py`
                                > *Code Insight:*
                                ```python
                                def _egg_link_names(raw_name: str) -> list[str]:
                                ```
                            📄 `entrypoints.py`
                                > *Code Insight:*
                                ```python
                                def _wrapper(args: list[str] | None = None) -> int:
                                ```
                            📄 `filesystem.py`
                                > *Code Insight:*
                                ```python
                                def check_path_owner(path: str) -> bool:
                                ```
                            📄 `filetypes.py`
                                > *Code Insight:*
                                ```python
                                def is_archive_file(name: str) -> bool:
                                ```
                            📄 `glibc.py`
                                > *Code Insight:*
                                ```python
                                def glibc_version_string() -> str | None:
                                ```
                            📄 `hashes.py`
                                > *Code Insight:*
                                ```python
                                class Hashes:
                                ```
                            📄 `logging.py`
                                > *Code Insight:*
                                ```python
                                class BrokenStdoutLoggingError(Exception):
                                ```
                            📄 `misc.py`
                                > *Code Insight:*
                                ```python
                                def get_pip_version() -> str:
                                ```
                            📄 `packaging.py`
                                > *Code Insight:*
                                ```python
                                def check_requires_python(
                                ```
                            📄 `retry.py`
                                > *Code Insight:*
                                ```python
                                def retry(
                                ```
                            📄 `subprocess.py`
                                > *Code Insight:*
                                ```python
                                def make_command(*args: str | HiddenText | CommandArgs) -> CommandArgs:
                                ```
                            📄 `temp_dir.py`
                                > *Code Insight:*
                                ```python
                                def global_tempdir_manager() -> Generator[None, None, None]:
                                ```
                            📄 `unpacking.py`
                                > *Code Insight:*
                                ```python
                                def current_umask() -> int:
                                ```
                            📄 `urls.py`
                                > *Code Insight:*
                                ```python
                                def path_to_url(path: str) -> str:
                                ```
                            📄 `virtualenv.py`
                                > *Code Insight:*
                                ```python
                                def _running_under_venv() -> bool:
                                ```
                            📄 `wheel.py`
                                > *Code Insight:*
                                ```python
                                def parse_wheel(wheel_zip: ZipFile, name: str) -> tuple[str, Message]:
                                ```
                            📄 `_jaraco_text.py`
                                > *Code Insight:*
                                ```python
                                def _nonblank(str):
                                ```
                            📄 `_log.py`
                                > *Code Insight:*
                                ```python
                                class VerboseLogger(logging.Logger):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **vcs/**
                            📄 `bazaar.py`
                                > *Code Insight:*
                                ```python
                                class Bazaar(VersionControl):
                                ```
                            📄 `git.py`
                                > *Code Insight:*
                                ```python
                                def looks_like_hash(sha: str) -> bool:
                                ```
                            📄 `mercurial.py`
                                > *Code Insight:*
                                ```python
                                class Mercurial(VersionControl):
                                ```
                            📄 `subversion.py`
                                > *Code Insight:*
                                ```python
                                class Subversion(VersionControl):
                                ```
                            📄 `versioncontrol.py`
                                > *Code Insight:*
                                ```python
                                def is_url(name: str) -> bool:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                    📂 **_vendor/**
                        📄 `README.rst`
                        📄 `vendor.txt`
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            def vendored(modulename):
                            ```
                        📂 **cachecontrol/**
                            📄 `adapter.py`
                                > *Code Insight:*
                                ```python
                                class CacheControlAdapter(HTTPAdapter):
                                ```
                            📄 `cache.py`
                                > *Code Insight:*
                                ```python
                                class BaseCache:
                                def get(self, key: str) -> bytes | None:
                                ```
                            📄 `controller.py`
                                > *Code Insight:*
                                ```python
                                def parse_uri(uri: str) -> tuple[str, str, str, str, str]:
                                ```
                            📄 `filewrapper.py`
                                > *Code Insight:*
                                ```python
                                class CallbackFileWrapper:
                                ```
                            📄 `heuristics.py`
                                > *Code Insight:*
                                ```python
                                def expire_after(delta: timedelta, date: datetime | None = None) -> datetime:
                                ```
                            📄 `LICENSE.txt`
                            📄 `py.typed`
                            📄 `serialize.py`
                                > *Code Insight:*
                                ```python
                                class Serializer:
                                ```
                            📄 `wrapper.py`
                                > *Code Insight:*
                                ```python
                                def CacheControl(
                                ```
                            📄 `_cmd.py`
                                > *Code Insight:*
                                ```python
                                def setup_logging() -> None:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **caches/**
                                📄 `file_cache.py`
                                    > *Code Insight:*
                                    ```python
                                    class _FileCacheMixin:
                                    ```
                                📄 `redis_cache.py`
                                    > *Code Insight:*
                                    ```python
                                    class RedisCache(BaseCache):
                                    def __init__(self, conn: Redis[bytes]) -> None:
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **certifi/**
                            📄 `cacert.pem`
                            📄 `core.py`
                                > *Code Insight:*
                                ```python
                                def exit_cacert_ctx() -> None:
                                ```
                            📄 `LICENSE`
                            📄 `py.typed`
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `__main__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **dependency_groups/**
                            📄 `LICENSE.txt`
                            📄 `py.typed`
                            📄 `_implementation.py`
                                > *Code Insight:*
                                ```python
                                def _normalize_name(name: str) -> str:
                                ```
                            📄 `_lint_dependency_groups.py`
                                > *Code Insight:*
                                ```python
                                def main(*, argv: list[str] | None = None) -> None:
                                ```
                            📄 `_pip_wrapper.py`
                                > *Code Insight:*
                                ```python
                                def _invoke_pip(deps: list[str]) -> None:
                                ```
                            📄 `_toml_compat.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `__main__.py`
                                > *Code Insight:*
                                ```python
                                def main() -> None:
                                ```
                        📂 **distlib/**
                            📄 `compat.py`
                                > *Code Insight:*
                                ```python
                                def quote(s):
                                ```
                            📄 `LICENSE.txt`
                            📄 `resources.py`
                                > *Code Insight:*
                                ```python
                                class ResourceCache(Cache):
                                def __init__(self, base=None):
                                ```
                            📄 `scripts.py`
                                > *Code Insight:*
                                ```python
                                def enquote_executable(executable):
                                ```
                            📄 `t32.exe`
                                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
                            📄 `t64-arm.exe`
                                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
                            📄 `t64.exe`
                                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
                            📄 `util.py`
                                > *Code Insight:*
                                ```python
                                def parse_marker(marker_string):
                                ```
                            📄 `w32.exe`
                                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
                            📄 `w64-arm.exe`
                                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
                            📄 `w64.exe`
                                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                class DistlibException(Exception):
                                ```
                        📂 **distro/**
                            📄 `distro.py`
                                > *Code Insight:*
                                ```python
                                class VersionDict(TypedDict):
                                ```
                            📄 `LICENSE`
                            📄 `py.typed`
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `__main__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **idna/**
                            📄 `codec.py`
                                > *Code Insight:*
                                ```python
                                class Codec(codecs.Codec):
                                def encode(self, data: str, errors: str = "strict") -> Tuple[bytes, int]:
                                ```
                            📄 `compat.py`
                                > *Code Insight:*
                                ```python
                                def ToASCII(label: str) -> bytes:
                                ```
                            📄 `core.py`
                                > *Code Insight:*
                                ```python
                                class IDNAError(UnicodeError):
                                ```
                            📄 `idnadata.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `intranges.py`
                                > *Code Insight:*
                                ```python
                                def intranges_from_list(list_: List[int]) -> Tuple[int, ...]:
                                ```
                            📄 `LICENSE.md`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `package_data.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `py.typed`
                            📄 `uts46data.py`
                                > *Code Insight:*
                                ```python
                                def _seg_0() -> List[Union[Tuple[int, str], Tuple[int, str, str]]]:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **msgpack/**
                            📄 `COPYING`
                            📄 `exceptions.py`
                                > *Code Insight:*
                                ```python
                                class UnpackException(Exception):
                                ```
                            📄 `ext.py`
                                > *Code Insight:*
                                ```python
                                class ExtType(namedtuple("ExtType", "code data")):
                                ```
                            📄 `fallback.py`
                                > *Code Insight:*
                                ```python
                                class BytesIO:
                                def __init__(self, s=b""):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def pack(o, stream, **kwargs):
                                ```
                        📂 **packaging/**
                            📄 `LICENSE`
                            📄 `LICENSE.APACHE`
                            📄 `LICENSE.BSD`
                            📄 `markers.py`
                                > *Code Insight:*
                                ```python
                                class InvalidMarker(ValueError):
                                ```
                            📄 `metadata.py`
                                > *Code Insight:*
                                ```python
                                class ExceptionGroup(Exception):
                                ```
                            📄 `py.typed`
                            📄 `requirements.py`
                                > *Code Insight:*
                                ```python
                                class InvalidRequirement(ValueError):
                                ```
                            📄 `specifiers.py`
                                > *Code Insight:*
                                ```python
                                def _coerce_version(version: UnparsedVersion) -> Version:
                                ```
                            📄 `tags.py`
                                > *Code Insight:*
                                ```python
                                class Tag:
                                ```
                            📄 `utils.py`
                                > *Code Insight:*
                                ```python
                                class InvalidName(ValueError):
                                ```
                            📄 `version.py`
                                > *Code Insight:*
                                ```python
                                class _Version(NamedTuple):
                                ```
                            📄 `_elffile.py`
                                > *Code Insight:*
                                ```python
                                class ELFInvalid(ValueError):
                                ```
                            📄 `_manylinux.py`
                                > *Code Insight:*
                                ```python
                                def _parse_elf(path: str) -> Generator[ELFFile | None, None, None]:
                                ```
                            📄 `_musllinux.py`
                                > *Code Insight:*
                                ```python
                                class _MuslVersion(NamedTuple):
                                ```
                            📄 `_parser.py`
                                > *Code Insight:*
                                ```python
                                class Node:
                                def __init__(self, value: str) -> None:
                                ```
                            📄 `_structures.py`
                                > *Code Insight:*
                                ```python
                                class InfinityType:
                                def __repr__(self) -> str:
                                ```
                            📄 `_tokenizer.py`
                                > *Code Insight:*
                                ```python
                                class Token:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **licenses/**
                                📄 `_spdx.py`
                                    > *Code Insight:*
                                    ```python
                                    class SPDXLicense(TypedDict):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    class InvalidLicenseExpression(ValueError):
                                    ```
                        📂 **pkg_resources/**
                            📄 `LICENSE`
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                class _LoaderProtocol(Protocol):
                                def load_module(self, fullname: str, /) -> types.ModuleType: ...
                                ```
                        📂 **platformdirs/**
                            📄 `android.py`
                                > *Code Insight:*
                                ```python
                                class Android(PlatformDirsABC):
                                ```
                            📄 `api.py`
                                > *Code Insight:*
                                ```python
                                class PlatformDirsABC(ABC):  # noqa: PLR0904
                                ```
                            📄 `LICENSE`
                            📄 `macos.py`
                                > *Code Insight:*
                                ```python
                                class MacOS(PlatformDirsABC):
                                ```
                            📄 `py.typed`
                            📄 `unix.py`
                                > *Code Insight:*
                                ```python
                                def getuid() -> NoReturn:
                                ```
                            📄 `version.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `windows.py`
                                > *Code Insight:*
                                ```python
                                class Windows(PlatformDirsABC):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def _set_platform_dir_class() -> type[PlatformDirsABC]:
                                ```
                            📄 `__main__.py`
                                > *Code Insight:*
                                ```python
                                def main() -> None:
                                ```
                        📂 **pygments/**
                            📄 `console.py`
                                > *Code Insight:*
                                ```python
                                def reset_color():
                                ```
                            📄 `filter.py`
                                > *Code Insight:*
                                ```python
                                def apply_filters(stream, filters, lexer=None):
                                def _apply(filter_, stream):
                                ```
                            📄 `formatter.py`
                                > *Code Insight:*
                                ```python
                                def _lookup_style(style):
                                ```
                            📄 `lexer.py`
                                > *Code Insight:*
                                ```python
                                class LexerMeta(type):
                                ```
                            📄 `LICENSE`
                            📄 `modeline.py`
                                > *Code Insight:*
                                ```python
                                def get_filetype_from_line(l): # noqa: E741
                                ```
                            📄 `plugin.py`
                                > *Code Insight:*
                                ```python
                                def iter_entry_points(group_name):
                                ```
                            📄 `regexopt.py`
                                > *Code Insight:*
                                ```python
                                def make_charset(letters):
                                ```
                            📄 `scanner.py`
                                > *Code Insight:*
                                ```python
                                class EndOfText(RuntimeError):
                                ```
                            📄 `sphinxext.py`
                                > *Code Insight:*
                                ```python
                                class PygmentsDoc(Directive):
                                ```
                            📄 `style.py`
                                > *Code Insight:*
                                ```python
                                class StyleMeta(type):
                                ```
                            📄 `token.py`
                                > *Code Insight:*
                                ```python
                                class _TokenType(tuple):
                                ```
                            📄 `unistring.py`
                                > *Code Insight:*
                                ```python
                                def combine(*args):
                                ```
                            📄 `util.py`
                                > *Code Insight:*
                                ```python
                                class ClassNotFound(ValueError):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def lex(code, lexer):
                                ```
                            📄 `__main__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **filters/**
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    def find_filter_class(filtername):
                                    ```
                            📂 **formatters/**
                                📄 `_mapping.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    def _fn_matches(fn, glob):
                                    ```
                            📂 **lexers/**
                                📄 `python.py`
                                    > *Code Insight:*
                                    ```python
                                    class PythonLexer(RegexLexer):
                                    ```
                                📄 `_mapping.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    def _fn_matches(fn, glob):
                                    ```
                            📂 **styles/**
                                📄 `_mapping.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    def get_style_by_name(name):
                                    ```
                        📂 **pyproject_hooks/**
                            📄 `LICENSE`
                            📄 `py.typed`
                            📄 `_impl.py`
                                > *Code Insight:*
                                ```python
                                class SubprocessRunner(Protocol):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **_in_process/**
                                📄 `_in_process.py`
                                    > *Code Insight:*
                                    ```python
                                    def write_json(obj, path, **kwargs):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    def _in_proc_script_path():
                                    ```
                        📂 **requests/**
                            📄 `adapters.py`
                                > *Code Insight:*
                                ```python
                                def SOCKSProxyManager(*args, **kwargs):
                                ```
                            📄 `api.py`
                                > *Code Insight:*
                                ```python
                                def request(method, url, **kwargs):
                                ```
                            📄 `auth.py`
                                > *Code Insight:*
                                ```python
                                def _basic_auth_str(username, password):
                                ```
                            📄 `certs.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `compat.py`
                                > *Code Insight:*
                                ```python
                                def _resolve_char_detection():
                                ```
                            📄 `cookies.py`
                                > *Code Insight:*
                                ```python
                                class MockRequest:
                                ```
                            📄 `exceptions.py`
                                > *Code Insight:*
                                ```python
                                class RequestException(IOError):
                                ```
                            📄 `help.py`
                                > *Code Insight:*
                                ```python
                                def _implementation():
                                ```
                            📄 `hooks.py`
                                > *Code Insight:*
                                ```python
                                def default_hooks():
                                ```
                            📄 `LICENSE`
                            📄 `models.py`
                                > *Code Insight:*
                                ```python
                                class RequestEncodingMixin:
                                def path_url(self):
                                ```
                            📄 `packages.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `sessions.py`
                                > *Code Insight:*
                                ```python
                                def merge_setting(request_setting, session_setting, dict_class=OrderedDict):
                                ```
                            📄 `status_codes.py`
                                > *Code Insight:*
                                ```python
                                def _init():
                                ```
                            📄 `structures.py`
                                > *Code Insight:*
                                ```python
                                class CaseInsensitiveDict(MutableMapping):
                                ```
                            📄 `utils.py`
                                > *Code Insight:*
                                ```python
                                def proxy_bypass_registry(host):
                                ```
                            📄 `_internal_utils.py`
                                > *Code Insight:*
                                ```python
                                def to_native_string(string, encoding="ascii"):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def check_compatibility(urllib3_version, chardet_version, charset_normalizer_version):
                                ```
                            📄 `__version__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **resolvelib/**
                            📄 `LICENSE`
                            📄 `providers.py`
                                > *Code Insight:*
                                ```python
                                class Preference(Protocol):
                                def __lt__(self, __other: Any) -> bool: ...
                                ```
                            📄 `py.typed`
                            📄 `reporters.py`
                                > *Code Insight:*
                                ```python
                                class BaseReporter(Generic[RT, CT, KT]):
                                ```
                            📄 `structs.py`
                                > *Code Insight:*
                                ```python
                                class RequirementInformation(NamedTuple, Generic[RT, CT]):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **resolvers/**
                                📄 `abstract.py`
                                    > *Code Insight:*
                                    ```python
                                    class Result(NamedTuple, Generic[RT, CT, KT]):
                                    ```
                                📄 `criterion.py`
                                    > *Code Insight:*
                                    ```python
                                    class Criterion(Generic[RT, CT]):
                                    ```
                                📄 `exceptions.py`
                                    > *Code Insight:*
                                    ```python
                                    class ResolverException(Exception):
                                    ```
                                📄 `resolution.py`
                                    > *Code Insight:*
                                    ```python
                                    def _build_result(state: State[RT, CT, KT]) -> Result[RT, CT, KT]:
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **rich/**
                            📄 `abc.py`
                                > *Code Insight:*
                                ```python
                                class RichRenderable(ABC):
                                ```
                            📄 `align.py`
                                > *Code Insight:*
                                ```python
                                class Align(JupyterMixin):
                                ```
                            📄 `ansi.py`
                                > *Code Insight:*
                                ```python
                                class _AnsiToken(NamedTuple):
                                ```
                            📄 `bar.py`
                                > *Code Insight:*
                                ```python
                                class Bar(JupyterMixin):
                                ```
                            📄 `box.py`
                                > *Code Insight:*
                                ```python
                                class Box:
                                ```
                            📄 `cells.py`
                                > *Code Insight:*
                                ```python
                                def cached_cell_len(text: str) -> int:
                                ```
                            📄 `color.py`
                                > *Code Insight:*
                                ```python
                                class ColorSystem(IntEnum):
                                ```
                            📄 `color_triplet.py`
                                > *Code Insight:*
                                ```python
                                class ColorTriplet(NamedTuple):
                                ```
                            📄 `columns.py`
                                > *Code Insight:*
                                ```python
                                class Columns(JupyterMixin):
                                ```
                            📄 `console.py`
                                > *Code Insight:*
                                ```python
                                class NoChange:
                                ```
                            📄 `constrain.py`
                                > *Code Insight:*
                                ```python
                                class Constrain(JupyterMixin):
                                ```
                            📄 `containers.py`
                                > *Code Insight:*
                                ```python
                                class Renderables:
                                ```
                            📄 `control.py`
                                > *Code Insight:*
                                ```python
                                class Control:
                                ```
                            📄 `default_styles.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `diagnose.py`
                                > *Code Insight:*
                                ```python
                                def report() -> None:  # pragma: no cover
                                ```
                            📄 `emoji.py`
                                > *Code Insight:*
                                ```python
                                class NoEmoji(Exception):
                                ```
                            📄 `errors.py`
                                > *Code Insight:*
                                ```python
                                class ConsoleError(Exception):
                                ```
                            📄 `filesize.py`
                                > *Code Insight:*
                                ```python
                                def _to_str(
                                ```
                            📄 `file_proxy.py`
                                > *Code Insight:*
                                ```python
                                class FileProxy(io.TextIOBase):
                                ```
                            📄 `highlighter.py`
                                > *Code Insight:*
                                ```python
                                def _combine_regex(*regexes: str) -> str:
                                ```
                            📄 `json.py`
                                > *Code Insight:*
                                ```python
                                class JSON:
                                ```
                            📄 `jupyter.py`
                                > *Code Insight:*
                                ```python
                                class JupyterRenderable:
                                ```
                            📄 `layout.py`
                                > *Code Insight:*
                                ```python
                                class LayoutRender(NamedTuple):
                                ```
                            📄 `LICENSE`
                            📄 `live.py`
                                > *Code Insight:*
                                ```python
                                class _RefreshThread(Thread):
                                ```
                            📄 `live_render.py`
                                > *Code Insight:*
                                ```python
                                class LiveRender:
                                ```
                            📄 `logging.py`
                                > *Code Insight:*
                                ```python
                                class RichHandler(Handler):
                                ```
                            📄 `markup.py`
                                > *Code Insight:*
                                ```python
                                class Tag(NamedTuple):
                                ```
                            📄 `measure.py`
                                > *Code Insight:*
                                ```python
                                class Measurement(NamedTuple):
                                ```
                            📄 `padding.py`
                                > *Code Insight:*
                                ```python
                                class Padding(JupyterMixin):
                                ```
                            📄 `pager.py`
                                > *Code Insight:*
                                ```python
                                class Pager(ABC):
                                ```
                            📄 `palette.py`
                                > *Code Insight:*
                                ```python
                                class Palette:
                                ```
                            📄 `panel.py`
                                > *Code Insight:*
                                ```python
                                class Panel(JupyterMixin):
                                ```
                            📄 `pretty.py`
                                > *Code Insight:*
                                ```python
                                def _is_attr_object(obj: Any) -> bool:
                                ```
                            📄 `progress.py`
                                > *Code Insight:*
                                ```python
                                class _TrackThread(Thread):
                                ```
                            📄 `progress_bar.py`
                                > *Code Insight:*
                                ```python
                                class ProgressBar(JupyterMixin):
                                ```
                            📄 `prompt.py`
                                > *Code Insight:*
                                ```python
                                class PromptError(Exception):
                                ```
                            📄 `protocol.py`
                                > *Code Insight:*
                                ```python
                                def is_renderable(check_object: Any) -> bool:
                                ```
                            📄 `py.typed`
                            📄 `region.py`
                                > *Code Insight:*
                                ```python
                                class Region(NamedTuple):
                                ```
                            📄 `repr.py`
                                > *Code Insight:*
                                ```python
                                class ReprError(Exception):
                                ```
                            📄 `rule.py`
                                > *Code Insight:*
                                ```python
                                class Rule(JupyterMixin):
                                ```
                            📄 `scope.py`
                                > *Code Insight:*
                                ```python
                                def render_scope(
                                ```
                            📄 `screen.py`
                                > *Code Insight:*
                                ```python
                                class Screen:
                                ```
                            📄 `segment.py`
                                > *Code Insight:*
                                ```python
                                class ControlType(IntEnum):
                                ```
                            📄 `spinner.py`
                                > *Code Insight:*
                                ```python
                                class Spinner:
                                ```
                            📄 `status.py`
                                > *Code Insight:*
                                ```python
                                class Status(JupyterMixin):
                                ```
                            📄 `style.py`
                                > *Code Insight:*
                                ```python
                                class _Bit:
                                ```
                            📄 `styled.py`
                                > *Code Insight:*
                                ```python
                                class Styled:
                                ```
                            📄 `syntax.py`
                                > *Code Insight:*
                                ```python
                                class SyntaxTheme(ABC):
                                ```
                            📄 `table.py`
                                > *Code Insight:*
                                ```python
                                class Column:
                                ```
                            📄 `terminal_theme.py`
                                > *Code Insight:*
                                ```python
                                class TerminalTheme:
                                ```
                            📄 `text.py`
                                > *Code Insight:*
                                ```python
                                class Span(NamedTuple):
                                ```
                            📄 `theme.py`
                                > *Code Insight:*
                                ```python
                                class Theme:
                                ```
                            📄 `themes.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `traceback.py`
                                > *Code Insight:*
                                ```python
                                def _iter_syntax_lines(
                                ```
                            📄 `tree.py`
                                > *Code Insight:*
                                ```python
                                class Tree(JupyterMixin):
                                ```
                            📄 `_cell_widths.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `_emoji_codes.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `_emoji_replace.py`
                                > *Code Insight:*
                                ```python
                                def _emoji_replace(
                                ```
                            📄 `_export_format.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `_extension.py`
                                > *Code Insight:*
                                ```python
                                def load_ipython_extension(ip: Any) -> None:  # pragma: no cover
                                ```
                            📄 `_fileno.py`
                                > *Code Insight:*
                                ```python
                                def get_fileno(file_like: IO[str]) -> int | None:
                                ```
                            📄 `_inspect.py`
                                > *Code Insight:*
                                ```python
                                def _first_paragraph(doc: str) -> str:
                                ```
                            📄 `_log_render.py`
                                > *Code Insight:*
                                ```python
                                class LogRender:
                                def __init__(
                                ```
                            📄 `_loop.py`
                                > *Code Insight:*
                                ```python
                                def loop_first(values: Iterable[T]) -> Iterable[Tuple[bool, T]]:
                                ```
                            📄 `_null_file.py`
                                > *Code Insight:*
                                ```python
                                class NullFile(IO[str]):
                                def close(self) -> None:
                                ```
                            📄 `_palettes.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `_pick.py`
                                > *Code Insight:*
                                ```python
                                def pick_bool(*values: Optional[bool]) -> bool:
                                ```
                            📄 `_ratio.py`
                                > *Code Insight:*
                                ```python
                                class Edge(Protocol):
                                ```
                            📄 `_spinners.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `_stack.py`
                                > *Code Insight:*
                                ```python
                                class Stack(List[T]):
                                ```
                            📄 `_timer.py`
                                > *Code Insight:*
                                ```python
                                def timer(subject: str = "time") -> Generator[None, None, None]:
                                ```
                            📄 `_win32_console.py`
                                > *Code Insight:*
                                ```python
                                class LegacyWindowsError(Exception):
                                ```
                            📄 `_windows.py`
                                > *Code Insight:*
                                ```python
                                class WindowsConsoleFeatures:
                                ```
                            📄 `_windows_renderer.py`
                                > *Code Insight:*
                                ```python
                                def legacy_windows_render(buffer: Iterable[Segment], term: LegacyWindowsTerm) -> None:
                                ```
                            📄 `_wrap.py`
                                > *Code Insight:*
                                ```python
                                def words(text: str) -> Iterable[tuple[int, int, str]]:
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def get_console() -> "Console":
                                ```
                            📄 `__main__.py`
                                > *Code Insight:*
                                ```python
                                class ColorBox:
                                def __rich_console__(
                                ```
                        📂 **tomli/**
                            📄 `LICENSE`
                            📄 `py.typed`
                            📄 `_parser.py`
                                > *Code Insight:*
                                ```python
                                class DEPRECATED_DEFAULT:
                                ```
                            📄 `_re.py`
                                > *Code Insight:*
                                ```python
                                def match_to_datetime(match: re.Match[str]) -> datetime | date:
                                ```
                            📄 `_types.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **tomli_w/**
                            📄 `LICENSE`
                            📄 `py.typed`
                            📄 `_writer.py`
                                > *Code Insight:*
                                ```python
                                class Context:
                                def __init__(self, allow_multiline: bool, indent: int):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **truststore/**
                            📄 `LICENSE`
                            📄 `py.typed`
                            📄 `_api.py`
                                > *Code Insight:*
                                ```python
                                def inject_into_ssl() -> None:
                                ```
                            📄 `_macos.py`
                                > *Code Insight:*
                                ```python
                                def _load_cdll(name: str, macos10_16_path: str) -> CDLL:
                                ```
                            📄 `_openssl.py`
                                > *Code Insight:*
                                ```python
                                def _configure_context(ctx: ssl.SSLContext) -> typing.Iterator[None]:
                                ```
                            📄 `_ssl_constants.py`
                                > *Code Insight:*
                                ```python
                                def _set_ssl_context_verify_mode(
                                ```
                            📄 `_windows.py`
                                > *Code Insight:*
                                ```python
                                class CERT_CONTEXT(Structure):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **urllib3/**
                            📄 `connection.py`
                                > *Code Insight:*
                                ```python
                                class BaseSSLError(BaseException):
                                ```
                            📄 `connectionpool.py`
                                > *Code Insight:*
                                ```python
                                class ConnectionPool(object):
                                ```
                            📄 `exceptions.py`
                                > *Code Insight:*
                                ```python
                                class HTTPError(Exception):
                                ```
                            📄 `fields.py`
                                > *Code Insight:*
                                ```python
                                def guess_content_type(filename, default="application/octet-stream"):
                                ```
                            📄 `filepost.py`
                                > *Code Insight:*
                                ```python
                                def choose_boundary():
                                ```
                            📄 `LICENSE.txt`
                            📄 `poolmanager.py`
                                > *Code Insight:*
                                ```python
                                def _default_key_normalizer(key_class, request_context):
                                ```
                            📄 `request.py`
                                > *Code Insight:*
                                ```python
                                class RequestMethods(object):
                                ```
                            📄 `response.py`
                                > *Code Insight:*
                                ```python
                                class DeflateDecoder(object):
                                def __init__(self):
                                ```
                            📄 `_collections.py`
                                > *Code Insight:*
                                ```python
                                class RLock:
                                def __enter__(self):
                                ```
                            📄 `_version.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def add_stderr_logger(level=logging.DEBUG):
                                ```
                            📂 **contrib/**
                                📄 `appengine.py`
                                    > *Code Insight:*
                                    ```python
                                    class AppEnginePlatformWarning(HTTPWarning):
                                    ```
                                📄 `ntlmpool.py`
                                    > *Code Insight:*
                                    ```python
                                    class NTLMConnectionPool(HTTPSConnectionPool):
                                    ```
                                📄 `pyopenssl.py`
                                    > *Code Insight:*
                                    ```python
                                    class UnsupportedExtension(Exception):
                                    ```
                                📄 `securetransport.py`
                                    > *Code Insight:*
                                    ```python
                                    def inject_into_urllib3():
                                    ```
                                📄 `socks.py`
                                    > *Code Insight:*
                                    ```python
                                    class SOCKSConnection(HTTPConnection):
                                    ```
                                📄 `_appengine_environ.py`
                                    > *Code Insight:*
                                    ```python
                                    def is_appengine():
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **_securetransport/**
                                    📄 `bindings.py`
                                        > *Code Insight:*
                                        ```python
                                        def load_cdll(name, macos10_16_path):
                                        ```
                                    📄 `low_level.py`
                                        > *Code Insight:*
                                        ```python
                                        def _cf_data_from_bytes(bytestring):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **packages/**
                                📄 `six.py`
                                    > *Code Insight:*
                                    ```python
                                    class X(object):
                                    def __len__(self):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **backports/**
                                    📄 `makefile.py`
                                        > *Code Insight:*
                                        ```python
                                        def backport_makefile(
                                        ```
                                    📄 `weakref_finalize.py`
                                        > *Code Insight:*
                                        ```python
                                        class weakref_finalize(object):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **util/**
                                📄 `connection.py`
                                    > *Code Insight:*
                                    ```python
                                    def is_connection_dropped(conn):  # Platform-specific
                                    ```
                                📄 `proxy.py`
                                    > *Code Insight:*
                                    ```python
                                    def connection_requires_http_tunnel(
                                    ```
                                📄 `queue.py`
                                    > *Code Insight:*
                                    ```python
                                    class LifoQueue(queue.Queue):
                                    def _init(self, _):
                                    ```
                                📄 `request.py`
                                    > *Code Insight:*
                                    ```python
                                    # ``Host``, and ``User-Agent``.
                                    ```
                                📄 `response.py`
                                    > *Code Insight:*
                                    ```python
                                    def is_fp_closed(obj):
                                    ```
                                📄 `retry.py`
                                    > *Code Insight:*
                                    ```python
                                    class _RetryMeta(type):
                                    def DEFAULT_METHOD_WHITELIST(cls):
                                    ```
                                📄 `ssltransport.py`
                                    > *Code Insight:*
                                    ```python
                                    class SSLTransport:
                                    ```
                                📄 `ssl_.py`
                                    > *Code Insight:*
                                    ```python
                                    def _const_compare_digest_backport(a, b):
                                    ```
                                📄 `ssl_match_hostname.py`
                                    > *Code Insight:*
                                    ```python
                                    class CertificateError(ValueError):
                                    ```
                                📄 `timeout.py`
                                    > *Code Insight:*
                                    ```python
                                    class Timeout(object):
                                    ```
                                📄 `url.py`
                                    > *Code Insight:*
                                    ```python
                                    class Url(namedtuple("Url", url_attrs)):
                                    ```
                                📄 `wait.py`
                                    > *Code Insight:*
                                    ```python
                                    class NoWayToWaitForSocketError(Exception):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                📂 **pip-25.3.dist-info/**
                    📄 `entry_points.txt`
                    📄 `INSTALLER`
                    📄 `METADATA`
                    📄 `RECORD`
                    📄 `REQUESTED`
                    📄 `WHEEL`
                    📂 **licenses/**
                        📄 `AUTHORS.txt`
                        📄 `LICENSE.txt`
                        📂 **src/**
                            📂 **pip/**
                                📂 **_vendor/**
                                    📂 **cachecontrol/**
                                        📄 `LICENSE.txt`
                                    📂 **certifi/**
                                        📄 `LICENSE`
                                    📂 **dependency_groups/**
                                        📄 `LICENSE.txt`
                                    📂 **distlib/**
                                        📄 `LICENSE.txt`
                                    📂 **distro/**
                                        📄 `LICENSE`
                                    📂 **idna/**
                                        📄 `LICENSE.md`
                                            > *Code Insight:*
                                            ```python
                                            ```
                                    📂 **msgpack/**
                                        📄 `COPYING`
                                    📂 **packaging/**
                                        📄 `LICENSE`
                                        📄 `LICENSE.APACHE`
                                        📄 `LICENSE.BSD`
                                    📂 **pkg_resources/**
                                        📄 `LICENSE`
                                    📂 **platformdirs/**
                                        📄 `LICENSE`
                                    📂 **pygments/**
                                        📄 `LICENSE`
                                    📂 **pyproject_hooks/**
                                        📄 `LICENSE`
                                    📂 **requests/**
                                        📄 `LICENSE`
                                    📂 **resolvelib/**
                                        📄 `LICENSE`
                                    📂 **rich/**
                                        📄 `LICENSE`
                                    📂 **tomli/**
                                        📄 `LICENSE`
                                    📂 **tomli_w/**
                                        📄 `LICENSE`
                                    📂 **truststore/**
                                        📄 `LICENSE`
                                    📂 **urllib3/**
                                        📄 `LICENSE.txt`
                📂 **plotly/**
                    📄 `animation.py`
                        > *Code Insight:*
                        ```python
                        class EasingValidator(EnumeratedValidator):
                        def __init__(self, plotly_name="easing", parent_name="batch_animate", **_):
                        ```
                    📄 `basedatatypes.py`
                        > *Code Insight:*
                        ```python
                        def _len_dict_item(item):
                        ```
                    📄 `basewidget.py`
                        > *Code Insight:*
                        ```python
                        class BaseFigureWidget(BaseFigure, anywidget.AnyWidget):
                        ```
                    📄 `callbacks.py`
                        > *Code Insight:*
                        ```python
                        class InputDeviceState:
                        def __init__(
                        ```
                    📄 `conftest.py`
                        > *Code Insight:*
                        ```python
                        def pytest_ignore_collect(path):
                        ```
                    📄 `exceptions.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `files.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `missing_anywidget.py`
                        > *Code Insight:*
                        ```python
                        class FigureWidget(BaseFigure):
                        ```
                    📄 `optional_imports.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📄 `serializers.py`
                        > *Code Insight:*
                        ```python
                        def _py_to_js(v, widget_manager):
                        ```
                    📄 `shapeannotation.py`
                        > *Code Insight:*
                        ```python
                        def _mean(x):
                        ```
                    📄 `subplots.py`
                        > *Code Insight:*
                        ```python
                        def make_subplots(
                        ```
                    📄 `tools.py`
                        > *Code Insight:*
                        ```python
                        def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
                        ```
                    📄 `utils.py`
                        > *Code Insight:*
                        ```python
                        def _list_repr_elided(v, threshold=200, edgeitems=3, indent=0, width=80):
                        ```
                    📄 `validator_cache.py`
                        > *Code Insight:*
                        ```python
                        class ValidatorCache(object):
                        ```
                    📄 `_subplots.py`
                        > *Code Insight:*
                        ```python
                        def _get_initial_max_subplot_ids():
                        ```
                    📄 `__init__.py`
                        > *Code Insight:*
                        ```python
                        def plot(data_frame, kind, **kwargs):
                        ```
                    📂 **api/**
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **colors/**
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **data/**
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            def gapminder(
                            ```
                    📂 **express/**
                        📄 `imshow_utils.py`
                            > *Code Insight:*
                            ```python
                            def intensity_range(image, range_values="image", clip_negative=False):
                            ```
                        📄 `_chart_types.py`
                            > *Code Insight:*
                            ```python
                            def scatter(
                            ```
                        📄 `_core.py`
                            > *Code Insight:*
                            ```python
                            class PxDefaults(object):
                            ```
                        📄 `_doc.py`
                            > *Code Insight:*
                            ```python
                            def make_docstring(fn, override_dict=None, append_dict=None):
                            ```
                        📄 `_imshow.py`
                            > *Code Insight:*
                            ```python
                            def _vectorize_zvalue(z, mode="max"):
                            ```
                        📄 `_special_inputs.py`
                            > *Code Insight:*
                            ```python
                            class IdentityMap(object):
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📂 **colors/**
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **data/**
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                        📂 **trendline_functions/**
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                def ols(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
                                ```
                    📂 **figure_factory/**
                        📄 `utils.py`
                            > *Code Insight:*
                            ```python
                            def is_sequence(obj):
                            ```
                        📄 `_2d_density.py`
                            > *Code Insight:*
                            ```python
                            def make_linear_colorscale(colors):
                            ```
                        📄 `_annotated_heatmap.py`
                            > *Code Insight:*
                            ```python
                            def validate_annotated_heatmap(z, x, y, annotation_text):
                            ```
                        📄 `_bullet.py`
                            > *Code Insight:*
                            ```python
                            def _bullet(
                            ```
                        📄 `_candlestick.py`
                            > *Code Insight:*
                            ```python
                            def make_increasing_candle(open, high, low, close, dates, **kwargs):
                            ```
                        📄 `_county_choropleth.py`
                            > *Code Insight:*
                            ```python
                            def _create_us_counties_df(st_to_state_name_dict, state_to_st_dict):
                            ```
                        📄 `_dendrogram.py`
                            > *Code Insight:*
                            ```python
                            def create_dendrogram(
                            ```
                        📄 `_distplot.py`
                            > *Code Insight:*
                            ```python
                            def validate_distplot(hist_data, curve_type):
                            ```
                        📄 `_facet_grid.py`
                            > *Code Insight:*
                            ```python
                            def _is_flipped(num):
                            ```
                        📄 `_gantt.py`
                            > *Code Insight:*
                            ```python
                            def _get_corner_points(x0, y0, x1, y1):
                            ```
                        📄 `_hexbin_map.py`
                            > *Code Insight:*
                            ```python
                            def _project_latlon_to_wgs84(lat, lon):
                            ```
                        📄 `_ohlc.py`
                            > *Code Insight:*
                            ```python
                            def validate_ohlc(open, high, low, close, direction, **kwargs):
                            ```
                        📄 `_quiver.py`
                            > *Code Insight:*
                            ```python
                            def create_quiver(
                            ```
                        📄 `_scatterplot.py`
                            > *Code Insight:*
                            ```python
                            def endpts_to_intervals(endpts):
                            ```
                        📄 `_streamline.py`
                            > *Code Insight:*
                            ```python
                            def validate_streamline(x, y):
                            ```
                        📄 `_table.py`
                            > *Code Insight:*
                            ```python
                            def validate_table(table_text, font_colors):
                            ```
                        📄 `_ternary_contour.py`
                            > *Code Insight:*
                            ```python
                            def _ternary_layout(
                            ```
                        📄 `_trisurf.py`
                            > *Code Insight:*
                            ```python
                            def map_face2color(face, colormap, scale, vmin, vmax):
                            ```
                        📄 `_violin.py`
                            > *Code Insight:*
                            ```python
                            def calc_stats(data):
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            def create_choropleth(*args, **kwargs):
                            ```
                    📂 **graph_objects/**
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            def __getattr__(import_name):
                            ```
                    📂 **graph_objs/**
                        📄 `graph_objs.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `_bar.py`
                            > *Code Insight:*
                            ```python
                            class Bar(_BaseTraceType):
                            ```
                        📄 `_barpolar.py`
                            > *Code Insight:*
                            ```python
                            class Barpolar(_BaseTraceType):
                            ```
                        📄 `_box.py`
                            > *Code Insight:*
                            ```python
                            class Box(_BaseTraceType):
                            ```
                        📄 `_candlestick.py`
                            > *Code Insight:*
                            ```python
                            class Candlestick(_BaseTraceType):
                            ```
                        📄 `_carpet.py`
                            > *Code Insight:*
                            ```python
                            class Carpet(_BaseTraceType):
                            ```
                        📄 `_choropleth.py`
                            > *Code Insight:*
                            ```python
                            class Choropleth(_BaseTraceType):
                            ```
                        📄 `_choroplethmap.py`
                            > *Code Insight:*
                            ```python
                            class Choroplethmap(_BaseTraceType):
                            ```
                        📄 `_choroplethmapbox.py`
                            > *Code Insight:*
                            ```python
                            class Choroplethmapbox(_BaseTraceType):
                            ```
                        📄 `_cone.py`
                            > *Code Insight:*
                            ```python
                            class Cone(_BaseTraceType):
                            ```
                        📄 `_contour.py`
                            > *Code Insight:*
                            ```python
                            class Contour(_BaseTraceType):
                            ```
                        📄 `_contourcarpet.py`
                            > *Code Insight:*
                            ```python
                            class Contourcarpet(_BaseTraceType):
                            ```
                        📄 `_densitymap.py`
                            > *Code Insight:*
                            ```python
                            class Densitymap(_BaseTraceType):
                            ```
                        📄 `_densitymapbox.py`
                            > *Code Insight:*
                            ```python
                            class Densitymapbox(_BaseTraceType):
                            ```
                        📄 `_deprecations.py`
                            > *Code Insight:*
                            ```python
                            class Data(list):
                            ```
                        📄 `_figure.py`
                            > *Code Insight:*
                            ```python
                            class Figure(BaseFigure):
                            def __init__(
                            ```
                        📄 `_figurewidget.py`
                            > *Code Insight:*
                            ```python
                            class FigureWidget(BaseFigureWidget):
                            def __init__(
                            ```
                        📄 `_frame.py`
                            > *Code Insight:*
                            ```python
                            class Frame(_BaseFrameHierarchyType):
                            ```
                        📄 `_funnel.py`
                            > *Code Insight:*
                            ```python
                            class Funnel(_BaseTraceType):
                            ```
                        📄 `_funnelarea.py`
                            > *Code Insight:*
                            ```python
                            class Funnelarea(_BaseTraceType):
                            ```
                        📄 `_heatmap.py`
                            > *Code Insight:*
                            ```python
                            class Heatmap(_BaseTraceType):
                            ```
                        📄 `_histogram.py`
                            > *Code Insight:*
                            ```python
                            class Histogram(_BaseTraceType):
                            ```
                        📄 `_histogram2d.py`
                            > *Code Insight:*
                            ```python
                            class Histogram2d(_BaseTraceType):
                            ```
                        📄 `_histogram2dcontour.py`
                            > *Code Insight:*
                            ```python
                            class Histogram2dContour(_BaseTraceType):
                            ```
                        📄 `_icicle.py`
                            > *Code Insight:*
                            ```python
                            class Icicle(_BaseTraceType):
                            ```
                        📄 `_image.py`
                            > *Code Insight:*
                            ```python
                            class Image(_BaseTraceType):
                            ```
                        📄 `_indicator.py`
                            > *Code Insight:*
                            ```python
                            class Indicator(_BaseTraceType):
                            ```
                        📄 `_isosurface.py`
                            > *Code Insight:*
                            ```python
                            class Isosurface(_BaseTraceType):
                            ```
                        📄 `_layout.py`
                            > *Code Insight:*
                            ```python
                            class Layout(_BaseLayoutType):
                            ```
                        📄 `_mesh3d.py`
                            > *Code Insight:*
                            ```python
                            class Mesh3d(_BaseTraceType):
                            ```
                        📄 `_ohlc.py`
                            > *Code Insight:*
                            ```python
                            class Ohlc(_BaseTraceType):
                            ```
                        📄 `_parcats.py`
                            > *Code Insight:*
                            ```python
                            class Parcats(_BaseTraceType):
                            ```
                        📄 `_parcoords.py`
                            > *Code Insight:*
                            ```python
                            class Parcoords(_BaseTraceType):
                            ```
                        📄 `_pie.py`
                            > *Code Insight:*
                            ```python
                            class Pie(_BaseTraceType):
                            ```
                        📄 `_sankey.py`
                            > *Code Insight:*
                            ```python
                            class Sankey(_BaseTraceType):
                            ```
                        📄 `_scatter.py`
                            > *Code Insight:*
                            ```python
                            class Scatter(_BaseTraceType):
                            ```
                        📄 `_scatter3d.py`
                            > *Code Insight:*
                            ```python
                            class Scatter3d(_BaseTraceType):
                            ```
                        📄 `_scattercarpet.py`
                            > *Code Insight:*
                            ```python
                            class Scattercarpet(_BaseTraceType):
                            ```
                        📄 `_scattergeo.py`
                            > *Code Insight:*
                            ```python
                            class Scattergeo(_BaseTraceType):
                            ```
                        📄 `_scattergl.py`
                            > *Code Insight:*
                            ```python
                            class Scattergl(_BaseTraceType):
                            ```
                        📄 `_scattermap.py`
                            > *Code Insight:*
                            ```python
                            class Scattermap(_BaseTraceType):
                            ```
                        📄 `_scattermapbox.py`
                            > *Code Insight:*
                            ```python
                            class Scattermapbox(_BaseTraceType):
                            ```
                        📄 `_scatterpolar.py`
                            > *Code Insight:*
                            ```python
                            class Scatterpolar(_BaseTraceType):
                            ```
                        📄 `_scatterpolargl.py`
                            > *Code Insight:*
                            ```python
                            class Scatterpolargl(_BaseTraceType):
                            ```
                        📄 `_scattersmith.py`
                            > *Code Insight:*
                            ```python
                            class Scattersmith(_BaseTraceType):
                            ```
                        📄 `_scatterternary.py`
                            > *Code Insight:*
                            ```python
                            class Scatterternary(_BaseTraceType):
                            ```
                        📄 `_splom.py`
                            > *Code Insight:*
                            ```python
                            class Splom(_BaseTraceType):
                            ```
                        📄 `_streamtube.py`
                            > *Code Insight:*
                            ```python
                            class Streamtube(_BaseTraceType):
                            ```
                        📄 `_sunburst.py`
                            > *Code Insight:*
                            ```python
                            class Sunburst(_BaseTraceType):
                            ```
                        📄 `_surface.py`
                            > *Code Insight:*
                            ```python
                            class Surface(_BaseTraceType):
                            ```
                        📄 `_table.py`
                            > *Code Insight:*
                            ```python
                            class Table(_BaseTraceType):
                            ```
                        📄 `_treemap.py`
                            > *Code Insight:*
                            ```python
                            class Treemap(_BaseTraceType):
                            ```
                        📄 `_violin.py`
                            > *Code Insight:*
                            ```python
                            class Violin(_BaseTraceType):
                            ```
                        📄 `_volume.py`
                            > *Code Insight:*
                            ```python
                            class Volume(_BaseTraceType):
                            ```
                        📄 `_waterfall.py`
                            > *Code Insight:*
                            ```python
                            class Waterfall(_BaseTraceType):
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            def __getattr__(import_name):
                            ```
                        📂 **bar/**
                            📄 `_error_x.py`
                                > *Code Insight:*
                                ```python
                                class ErrorX(_BaseTraceHierarchyType):
                                ```
                            📄 `_error_y.py`
                                > *Code Insight:*
                                ```python
                                class ErrorY(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_outsidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Outsidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pattern.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pattern(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **barpolar/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pattern.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pattern(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **box/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **candlestick/**
                            📄 `_decreasing.py`
                                > *Code Insight:*
                                ```python
                                class Decreasing(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_increasing.py`
                                > *Code Insight:*
                                ```python
                                class Increasing(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **decreasing/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **increasing/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **carpet/**
                            📄 `_aaxis.py`
                                > *Code Insight:*
                                ```python
                                class Aaxis(_BaseTraceHierarchyType):
                                ```
                            📄 `_baxis.py`
                                > *Code Insight:*
                                ```python
                                class Baxis(_BaseTraceHierarchyType):
                                ```
                            📄 `_font.py`
                                > *Code Insight:*
                                ```python
                                class Font(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **aaxis/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **baxis/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **choropleth/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **choroplethmap/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **choroplethmapbox/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **cone/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_lighting.py`
                                > *Code Insight:*
                                ```python
                                class Lighting(_BaseTraceHierarchyType):
                                ```
                            📄 `_lightposition.py`
                                > *Code Insight:*
                                ```python
                                class Lightposition(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **contour/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_contours.py`
                                > *Code Insight:*
                                ```python
                                class Contours(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **contours/**
                                📄 `_labelfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Labelfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **contourcarpet/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_contours.py`
                                > *Code Insight:*
                                ```python
                                class Contours(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **contours/**
                                📄 `_labelfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Labelfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **densitymap/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **densitymapbox/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **funnel/**
                            📄 `_connector.py`
                                > *Code Insight:*
                                ```python
                                class Connector(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_outsidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Outsidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **connector/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                        📂 **funnelarea/**
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_title.py`
                                > *Code Insight:*
                                ```python
                                class Title(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pattern.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pattern(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **title/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **heatmap/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **histogram/**
                            📄 `_cumulative.py`
                                > *Code Insight:*
                                ```python
                                class Cumulative(_BaseTraceHierarchyType):
                                ```
                            📄 `_error_x.py`
                                > *Code Insight:*
                                ```python
                                class ErrorX(_BaseTraceHierarchyType):
                                ```
                            📄 `_error_y.py`
                                > *Code Insight:*
                                ```python
                                class ErrorY(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_outsidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Outsidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `_xbins.py`
                                > *Code Insight:*
                                ```python
                                class XBins(_BaseTraceHierarchyType):
                                ```
                            📄 `_ybins.py`
                                > *Code Insight:*
                                ```python
                                class YBins(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pattern.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pattern(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **histogram2d/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_xbins.py`
                                > *Code Insight:*
                                ```python
                                class XBins(_BaseTraceHierarchyType):
                                ```
                            📄 `_ybins.py`
                                > *Code Insight:*
                                ```python
                                class YBins(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **histogram2dcontour/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_contours.py`
                                > *Code Insight:*
                                ```python
                                class Contours(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_xbins.py`
                                > *Code Insight:*
                                ```python
                                class XBins(_BaseTraceHierarchyType):
                                ```
                            📄 `_ybins.py`
                                > *Code Insight:*
                                ```python
                                class YBins(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **contours/**
                                📄 `_labelfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Labelfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **icicle/**
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_leaf.py`
                                > *Code Insight:*
                                ```python
                                class Leaf(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_outsidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Outsidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_pathbar.py`
                                > *Code Insight:*
                                ```python
                                class Pathbar(_BaseTraceHierarchyType):
                                ```
                            📄 `_root.py`
                                > *Code Insight:*
                                ```python
                                class Root(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_tiling.py`
                                > *Code Insight:*
                                ```python
                                class Tiling(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pattern.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pattern(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **pathbar/**
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **image/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **indicator/**
                            📄 `_delta.py`
                                > *Code Insight:*
                                ```python
                                class Delta(_BaseTraceHierarchyType):
                                ```
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_gauge.py`
                                > *Code Insight:*
                                ```python
                                class Gauge(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_number.py`
                                > *Code Insight:*
                                ```python
                                class Number(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_title.py`
                                > *Code Insight:*
                                ```python
                                class Title(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **delta/**
                                📄 `_decreasing.py`
                                    > *Code Insight:*
                                    ```python
                                    class Decreasing(_BaseTraceHierarchyType):
                                    ```
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `_increasing.py`
                                    > *Code Insight:*
                                    ```python
                                    class Increasing(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **gauge/**
                                📄 `_axis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Axis(_BaseTraceHierarchyType):
                                    ```
                                📄 `_bar.py`
                                    > *Code Insight:*
                                    ```python
                                    class Bar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_step.py`
                                    > *Code Insight:*
                                    ```python
                                    class Step(_BaseTraceHierarchyType):
                                    ```
                                📄 `_threshold.py`
                                    > *Code Insight:*
                                    ```python
                                    class Threshold(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **axis/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **bar/**
                                    📄 `_line.py`
                                        > *Code Insight:*
                                        ```python
                                        class Line(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **step/**
                                    📄 `_line.py`
                                        > *Code Insight:*
                                        ```python
                                        class Line(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **threshold/**
                                    📄 `_line.py`
                                        > *Code Insight:*
                                        ```python
                                        class Line(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **number/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **title/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **isosurface/**
                            📄 `_caps.py`
                                > *Code Insight:*
                                ```python
                                class Caps(_BaseTraceHierarchyType):
                                ```
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_contour.py`
                                > *Code Insight:*
                                ```python
                                class Contour(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_lighting.py`
                                > *Code Insight:*
                                ```python
                                class Lighting(_BaseTraceHierarchyType):
                                ```
                            📄 `_lightposition.py`
                                > *Code Insight:*
                                ```python
                                class Lightposition(_BaseTraceHierarchyType):
                                ```
                            📄 `_slices.py`
                                > *Code Insight:*
                                ```python
                                class Slices(_BaseTraceHierarchyType):
                                ```
                            📄 `_spaceframe.py`
                                > *Code Insight:*
                                ```python
                                class Spaceframe(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_surface.py`
                                > *Code Insight:*
                                ```python
                                class Surface(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **caps/**
                                📄 `_x.py`
                                    > *Code Insight:*
                                    ```python
                                    class X(_BaseTraceHierarchyType):
                                    ```
                                📄 `_y.py`
                                    > *Code Insight:*
                                    ```python
                                    class Y(_BaseTraceHierarchyType):
                                    ```
                                📄 `_z.py`
                                    > *Code Insight:*
                                    ```python
                                    class Z(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **slices/**
                                📄 `_x.py`
                                    > *Code Insight:*
                                    ```python
                                    class X(_BaseTraceHierarchyType):
                                    ```
                                📄 `_y.py`
                                    > *Code Insight:*
                                    ```python
                                    class Y(_BaseTraceHierarchyType):
                                    ```
                                📄 `_z.py`
                                    > *Code Insight:*
                                    ```python
                                    class Z(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **layout/**
                            📄 `_activeselection.py`
                                > *Code Insight:*
                                ```python
                                class Activeselection(_BaseLayoutHierarchyType):
                                ```
                            📄 `_activeshape.py`
                                > *Code Insight:*
                                ```python
                                class Activeshape(_BaseLayoutHierarchyType):
                                ```
                            📄 `_annotation.py`
                                > *Code Insight:*
                                ```python
                                class Annotation(_BaseLayoutHierarchyType):
                                ```
                            📄 `_coloraxis.py`
                                > *Code Insight:*
                                ```python
                                class Coloraxis(_BaseLayoutHierarchyType):
                                ```
                            📄 `_colorscale.py`
                                > *Code Insight:*
                                ```python
                                class Colorscale(_BaseLayoutHierarchyType):
                                ```
                            📄 `_font.py`
                                > *Code Insight:*
                                ```python
                                class Font(_BaseLayoutHierarchyType):
                                ```
                            📄 `_geo.py`
                                > *Code Insight:*
                                ```python
                                class Geo(_BaseLayoutHierarchyType):
                                ```
                            📄 `_grid.py`
                                > *Code Insight:*
                                ```python
                                class Grid(_BaseLayoutHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseLayoutHierarchyType):
                                ```
                            📄 `_image.py`
                                > *Code Insight:*
                                ```python
                                class Image(_BaseLayoutHierarchyType):
                                ```
                            📄 `_legend.py`
                                > *Code Insight:*
                                ```python
                                class Legend(_BaseLayoutHierarchyType):
                                ```
                            📄 `_map.py`
                                > *Code Insight:*
                                ```python
                                class Map(_BaseLayoutHierarchyType):
                                ```
                            📄 `_mapbox.py`
                                > *Code Insight:*
                                ```python
                                class Mapbox(_BaseLayoutHierarchyType):
                                ```
                            📄 `_margin.py`
                                > *Code Insight:*
                                ```python
                                class Margin(_BaseLayoutHierarchyType):
                                ```
                            📄 `_modebar.py`
                                > *Code Insight:*
                                ```python
                                class Modebar(_BaseLayoutHierarchyType):
                                ```
                            📄 `_newselection.py`
                                > *Code Insight:*
                                ```python
                                class Newselection(_BaseLayoutHierarchyType):
                                ```
                            📄 `_newshape.py`
                                > *Code Insight:*
                                ```python
                                class Newshape(_BaseLayoutHierarchyType):
                                ```
                            📄 `_polar.py`
                                > *Code Insight:*
                                ```python
                                class Polar(_BaseLayoutHierarchyType):
                                ```
                            📄 `_scene.py`
                                > *Code Insight:*
                                ```python
                                class Scene(_BaseLayoutHierarchyType):
                                ```
                            📄 `_selection.py`
                                > *Code Insight:*
                                ```python
                                class Selection(_BaseLayoutHierarchyType):
                                ```
                            📄 `_shape.py`
                                > *Code Insight:*
                                ```python
                                class Shape(_BaseLayoutHierarchyType):
                                ```
                            📄 `_slider.py`
                                > *Code Insight:*
                                ```python
                                class Slider(_BaseLayoutHierarchyType):
                                ```
                            📄 `_smith.py`
                                > *Code Insight:*
                                ```python
                                class Smith(_BaseLayoutHierarchyType):
                                ```
                            📄 `_template.py`
                                > *Code Insight:*
                                ```python
                                class Template(_BaseLayoutHierarchyType):
                                ```
                            📄 `_ternary.py`
                                > *Code Insight:*
                                ```python
                                class Ternary(_BaseLayoutHierarchyType):
                                ```
                            📄 `_title.py`
                                > *Code Insight:*
                                ```python
                                class Title(_BaseLayoutHierarchyType):
                                ```
                            📄 `_transition.py`
                                > *Code Insight:*
                                ```python
                                class Transition(_BaseLayoutHierarchyType):
                                ```
                            📄 `_uniformtext.py`
                                > *Code Insight:*
                                ```python
                                class Uniformtext(_BaseLayoutHierarchyType):
                                ```
                            📄 `_updatemenu.py`
                                > *Code Insight:*
                                ```python
                                class Updatemenu(_BaseLayoutHierarchyType):
                                ```
                            📄 `_xaxis.py`
                                > *Code Insight:*
                                ```python
                                class XAxis(_BaseLayoutHierarchyType):
                                ```
                            📄 `_yaxis.py`
                                > *Code Insight:*
                                ```python
                                class YAxis(_BaseLayoutHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **annotation/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_hoverlabel.py`
                                    > *Code Insight:*
                                    ```python
                                    class Hoverlabel(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **hoverlabel/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **coloraxis/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **geo/**
                                📄 `_center.py`
                                    > *Code Insight:*
                                    ```python
                                    class Center(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_domain.py`
                                    > *Code Insight:*
                                    ```python
                                    class Domain(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_lataxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Lataxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_lonaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Lonaxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_projection.py`
                                    > *Code Insight:*
                                    ```python
                                    class Projection(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **projection/**
                                    📄 `_rotation.py`
                                        > *Code Insight:*
                                        ```python
                                        class Rotation(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **grid/**
                                📄 `_domain.py`
                                    > *Code Insight:*
                                    ```python
                                    class Domain(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_grouptitlefont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Grouptitlefont(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legend/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_grouptitlefont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Grouptitlefont(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **map/**
                                📄 `_bounds.py`
                                    > *Code Insight:*
                                    ```python
                                    class Bounds(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_center.py`
                                    > *Code Insight:*
                                    ```python
                                    class Center(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_domain.py`
                                    > *Code Insight:*
                                    ```python
                                    class Domain(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_layer.py`
                                    > *Code Insight:*
                                    ```python
                                    class Layer(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **layer/**
                                    📄 `_circle.py`
                                        > *Code Insight:*
                                        ```python
                                        class Circle(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_fill.py`
                                        > *Code Insight:*
                                        ```python
                                        class Fill(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_line.py`
                                        > *Code Insight:*
                                        ```python
                                        class Line(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_symbol.py`
                                        > *Code Insight:*
                                        ```python
                                        class Symbol(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **symbol/**
                                        📄 `_textfont.py`
                                            > *Code Insight:*
                                            ```python
                                            class Textfont(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **mapbox/**
                                📄 `_bounds.py`
                                    > *Code Insight:*
                                    ```python
                                    class Bounds(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_center.py`
                                    > *Code Insight:*
                                    ```python
                                    class Center(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_domain.py`
                                    > *Code Insight:*
                                    ```python
                                    class Domain(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_layer.py`
                                    > *Code Insight:*
                                    ```python
                                    class Layer(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **layer/**
                                    📄 `_circle.py`
                                        > *Code Insight:*
                                        ```python
                                        class Circle(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_fill.py`
                                        > *Code Insight:*
                                        ```python
                                        class Fill(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_line.py`
                                        > *Code Insight:*
                                        ```python
                                        class Line(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_symbol.py`
                                        > *Code Insight:*
                                        ```python
                                        class Symbol(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **symbol/**
                                        📄 `_textfont.py`
                                            > *Code Insight:*
                                            ```python
                                            class Textfont(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **newselection/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **newshape/**
                                📄 `_label.py`
                                    > *Code Insight:*
                                    ```python
                                    class Label(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_legendgrouptitle.py`
                                    > *Code Insight:*
                                    ```python
                                    class Legendgrouptitle(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **label/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **legendgrouptitle/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **polar/**
                                📄 `_angularaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class AngularAxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_domain.py`
                                    > *Code Insight:*
                                    ```python
                                    class Domain(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_radialaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class RadialAxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **angularaxis/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **radialaxis/**
                                    📄 `_autorangeoptions.py`
                                        > *Code Insight:*
                                        ```python
                                        class Autorangeoptions(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **scene/**
                                📄 `_annotation.py`
                                    > *Code Insight:*
                                    ```python
                                    class Annotation(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_aspectratio.py`
                                    > *Code Insight:*
                                    ```python
                                    class Aspectratio(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_camera.py`
                                    > *Code Insight:*
                                    ```python
                                    class Camera(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_domain.py`
                                    > *Code Insight:*
                                    ```python
                                    class Domain(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_xaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class XAxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_yaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class YAxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_zaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class ZAxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **annotation/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_hoverlabel.py`
                                        > *Code Insight:*
                                        ```python
                                        class Hoverlabel(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **hoverlabel/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                                📂 **camera/**
                                    📄 `_center.py`
                                        > *Code Insight:*
                                        ```python
                                        class Center(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_eye.py`
                                        > *Code Insight:*
                                        ```python
                                        class Eye(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_projection.py`
                                        > *Code Insight:*
                                        ```python
                                        class Projection(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_up.py`
                                        > *Code Insight:*
                                        ```python
                                        class Up(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **xaxis/**
                                    📄 `_autorangeoptions.py`
                                        > *Code Insight:*
                                        ```python
                                        class Autorangeoptions(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                                📂 **yaxis/**
                                    📄 `_autorangeoptions.py`
                                        > *Code Insight:*
                                        ```python
                                        class Autorangeoptions(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                                📂 **zaxis/**
                                    📄 `_autorangeoptions.py`
                                        > *Code Insight:*
                                        ```python
                                        class Autorangeoptions(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selection/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **shape/**
                                📄 `_label.py`
                                    > *Code Insight:*
                                    ```python
                                    class Label(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_legendgrouptitle.py`
                                    > *Code Insight:*
                                    ```python
                                    class Legendgrouptitle(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **label/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **legendgrouptitle/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **slider/**
                                📄 `_currentvalue.py`
                                    > *Code Insight:*
                                    ```python
                                    class Currentvalue(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_pad.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pad(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_step.py`
                                    > *Code Insight:*
                                    ```python
                                    class Step(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_transition.py`
                                    > *Code Insight:*
                                    ```python
                                    class Transition(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **currentvalue/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **smith/**
                                📄 `_domain.py`
                                    > *Code Insight:*
                                    ```python
                                    class Domain(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_imaginaryaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Imaginaryaxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_realaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Realaxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **imaginaryaxis/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **realaxis/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **template/**
                                📄 `_data.py`
                                    > *Code Insight:*
                                    ```python
                                    class Data(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_layout.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **data/**
                                    📄 `_bar.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_barpolar.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_box.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_candlestick.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_carpet.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_choropleth.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_choroplethmap.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_choroplethmapbox.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_cone.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_contour.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_contourcarpet.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_densitymap.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_densitymapbox.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_funnel.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_funnelarea.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_heatmap.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_histogram.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_histogram2d.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_histogram2dcontour.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_icicle.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_image.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_indicator.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_isosurface.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_mesh3d.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_ohlc.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_parcats.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_parcoords.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_pie.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_sankey.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scatter.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scatter3d.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scattercarpet.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scattergeo.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scattergl.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scattermap.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scattermapbox.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scatterpolar.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scatterpolargl.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scattersmith.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_scatterternary.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_splom.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_streamtube.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_sunburst.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_surface.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_table.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_treemap.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_violin.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_volume.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `_waterfall.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **ternary/**
                                📄 `_aaxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Aaxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_baxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Baxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_caxis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Caxis(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_domain.py`
                                    > *Code Insight:*
                                    ```python
                                    class Domain(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **aaxis/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                                📂 **baxis/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                                📂 **caxis/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseLayoutHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **title/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_pad.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pad(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_subtitle.py`
                                    > *Code Insight:*
                                    ```python
                                    class Subtitle(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **subtitle/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **updatemenu/**
                                📄 `_button.py`
                                    > *Code Insight:*
                                    ```python
                                    class Button(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_pad.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pad(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **xaxis/**
                                📄 `_autorangeoptions.py`
                                    > *Code Insight:*
                                    ```python
                                    class Autorangeoptions(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_minor.py`
                                    > *Code Insight:*
                                    ```python
                                    class Minor(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_rangebreak.py`
                                    > *Code Insight:*
                                    ```python
                                    class Rangebreak(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_rangeselector.py`
                                    > *Code Insight:*
                                    ```python
                                    class Rangeselector(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_rangeslider.py`
                                    > *Code Insight:*
                                    ```python
                                    class Rangeslider(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_unifiedhovertitle.py`
                                    > *Code Insight:*
                                    ```python
                                    class Unifiedhovertitle(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **rangeselector/**
                                    📄 `_button.py`
                                        > *Code Insight:*
                                        ```python
                                        class Button(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **rangeslider/**
                                    📄 `_yaxis.py`
                                        > *Code Insight:*
                                        ```python
                                        class YAxis(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **yaxis/**
                                📄 `_autorangeoptions.py`
                                    > *Code Insight:*
                                    ```python
                                    class Autorangeoptions(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_minor.py`
                                    > *Code Insight:*
                                    ```python
                                    class Minor(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_rangebreak.py`
                                    > *Code Insight:*
                                    ```python
                                    class Rangebreak(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseLayoutHierarchyType):
                                    ```
                                📄 `_unifiedhovertitle.py`
                                    > *Code Insight:*
                                    ```python
                                    class Unifiedhovertitle(_BaseLayoutHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseLayoutHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                        📂 **mesh3d/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_contour.py`
                                > *Code Insight:*
                                ```python
                                class Contour(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_lighting.py`
                                > *Code Insight:*
                                ```python
                                class Lighting(_BaseTraceHierarchyType):
                                ```
                            📄 `_lightposition.py`
                                > *Code Insight:*
                                ```python
                                class Lightposition(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **ohlc/**
                            📄 `_decreasing.py`
                                > *Code Insight:*
                                ```python
                                class Decreasing(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_increasing.py`
                                > *Code Insight:*
                                ```python
                                class Increasing(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **decreasing/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **increasing/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **parcats/**
                            📄 `_dimension.py`
                                > *Code Insight:*
                                ```python
                                class Dimension(_BaseTraceHierarchyType):
                                ```
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_labelfont.py`
                                > *Code Insight:*
                                ```python
                                class Labelfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_tickfont.py`
                                > *Code Insight:*
                                ```python
                                class Tickfont(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **line/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                        📂 **parcoords/**
                            📄 `_dimension.py`
                                > *Code Insight:*
                                ```python
                                class Dimension(_BaseTraceHierarchyType):
                                ```
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_labelfont.py`
                                > *Code Insight:*
                                ```python
                                class Labelfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_rangefont.py`
                                > *Code Insight:*
                                ```python
                                class Rangefont(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_tickfont.py`
                                > *Code Insight:*
                                ```python
                                class Tickfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **line/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **unselected/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **pie/**
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_outsidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Outsidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_title.py`
                                > *Code Insight:*
                                ```python
                                class Title(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pattern.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pattern(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **title/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **sankey/**
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_link.py`
                                > *Code Insight:*
                                ```python
                                class Link(_BaseTraceHierarchyType):
                                ```
                            📄 `_node.py`
                                > *Code Insight:*
                                ```python
                                class Node(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **link/**
                                📄 `_colorscale.py`
                                    > *Code Insight:*
                                    ```python
                                    class Colorscale(_BaseTraceHierarchyType):
                                    ```
                                📄 `_hoverlabel.py`
                                    > *Code Insight:*
                                    ```python
                                    class Hoverlabel(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **hoverlabel/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **node/**
                                📄 `_hoverlabel.py`
                                    > *Code Insight:*
                                    ```python
                                    class Hoverlabel(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **hoverlabel/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                        📂 **scatter/**
                            📄 `_error_x.py`
                                > *Code Insight:*
                                ```python
                                class ErrorX(_BaseTraceHierarchyType):
                                ```
                            📄 `_error_y.py`
                                > *Code Insight:*
                                ```python
                                class ErrorY(_BaseTraceHierarchyType):
                                ```
                            📄 `_fillgradient.py`
                                > *Code Insight:*
                                ```python
                                class Fillgradient(_BaseTraceHierarchyType):
                                ```
                            📄 `_fillpattern.py`
                                > *Code Insight:*
                                ```python
                                class Fillpattern(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_gradient.py`
                                    > *Code Insight:*
                                    ```python
                                    class Gradient(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scatter3d/**
                            📄 `_error_x.py`
                                > *Code Insight:*
                                ```python
                                class ErrorX(_BaseTraceHierarchyType):
                                ```
                            📄 `_error_y.py`
                                > *Code Insight:*
                                ```python
                                class ErrorY(_BaseTraceHierarchyType):
                                ```
                            📄 `_error_z.py`
                                > *Code Insight:*
                                ```python
                                class ErrorZ(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_projection.py`
                                > *Code Insight:*
                                ```python
                                class Projection(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **line/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **projection/**
                                📄 `_x.py`
                                    > *Code Insight:*
                                    ```python
                                    class X(_BaseTraceHierarchyType):
                                    ```
                                📄 `_y.py`
                                    > *Code Insight:*
                                    ```python
                                    class Y(_BaseTraceHierarchyType):
                                    ```
                                📄 `_z.py`
                                    > *Code Insight:*
                                    ```python
                                    class Z(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scattercarpet/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_gradient.py`
                                    > *Code Insight:*
                                    ```python
                                    class Gradient(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scattergeo/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_gradient.py`
                                    > *Code Insight:*
                                    ```python
                                    class Gradient(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scattergl/**
                            📄 `_error_x.py`
                                > *Code Insight:*
                                ```python
                                class ErrorX(_BaseTraceHierarchyType):
                                ```
                            📄 `_error_y.py`
                                > *Code Insight:*
                                ```python
                                class ErrorY(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scattermap/**
                            📄 `_cluster.py`
                                > *Code Insight:*
                                ```python
                                class Cluster(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scattermapbox/**
                            📄 `_cluster.py`
                                > *Code Insight:*
                                ```python
                                class Cluster(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scatterpolar/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_gradient.py`
                                    > *Code Insight:*
                                    ```python
                                    class Gradient(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scatterpolargl/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scattersmith/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_gradient.py`
                                    > *Code Insight:*
                                    ```python
                                    class Gradient(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **scatterternary/**
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_gradient.py`
                                    > *Code Insight:*
                                    ```python
                                    class Gradient(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **splom/**
                            📄 `_diagonal.py`
                                > *Code Insight:*
                                ```python
                                class Diagonal(_BaseTraceHierarchyType):
                                ```
                            📄 `_dimension.py`
                                > *Code Insight:*
                                ```python
                                class Dimension(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **dimension/**
                                📄 `_axis.py`
                                    > *Code Insight:*
                                    ```python
                                    class Axis(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **streamtube/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_lighting.py`
                                > *Code Insight:*
                                ```python
                                class Lighting(_BaseTraceHierarchyType):
                                ```
                            📄 `_lightposition.py`
                                > *Code Insight:*
                                ```python
                                class Lightposition(_BaseTraceHierarchyType):
                                ```
                            📄 `_starts.py`
                                > *Code Insight:*
                                ```python
                                class Starts(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **sunburst/**
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_leaf.py`
                                > *Code Insight:*
                                ```python
                                class Leaf(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_outsidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Outsidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_root.py`
                                > *Code Insight:*
                                ```python
                                class Root(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pattern.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pattern(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                        📂 **surface/**
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_contours.py`
                                > *Code Insight:*
                                ```python
                                class Contours(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_lighting.py`
                                > *Code Insight:*
                                ```python
                                class Lighting(_BaseTraceHierarchyType):
                                ```
                            📄 `_lightposition.py`
                                > *Code Insight:*
                                ```python
                                class Lightposition(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **contours/**
                                📄 `_x.py`
                                    > *Code Insight:*
                                    ```python
                                    class X(_BaseTraceHierarchyType):
                                    ```
                                📄 `_y.py`
                                    > *Code Insight:*
                                    ```python
                                    class Y(_BaseTraceHierarchyType):
                                    ```
                                📄 `_z.py`
                                    > *Code Insight:*
                                    ```python
                                    class Z(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **x/**
                                    📄 `_project.py`
                                        > *Code Insight:*
                                        ```python
                                        class Project(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **y/**
                                    📄 `_project.py`
                                        > *Code Insight:*
                                        ```python
                                        class Project(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                📂 **z/**
                                    📄 `_project.py`
                                        > *Code Insight:*
                                        ```python
                                        class Project(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **table/**
                            📄 `_cells.py`
                                > *Code Insight:*
                                ```python
                                class Cells(_BaseTraceHierarchyType):
                                ```
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_header.py`
                                > *Code Insight:*
                                ```python
                                class Header(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **cells/**
                                📄 `_fill.py`
                                    > *Code Insight:*
                                    ```python
                                    class Fill(_BaseTraceHierarchyType):
                                    ```
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **header/**
                                📄 `_fill.py`
                                    > *Code Insight:*
                                    ```python
                                    class Fill(_BaseTraceHierarchyType):
                                    ```
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **treemap/**
                            📄 `_domain.py`
                                > *Code Insight:*
                                ```python
                                class Domain(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_outsidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Outsidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_pathbar.py`
                                > *Code Insight:*
                                ```python
                                class Pathbar(_BaseTraceHierarchyType):
                                ```
                            📄 `_root.py`
                                > *Code Insight:*
                                ```python
                                class Root(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_tiling.py`
                                > *Code Insight:*
                                ```python
                                class Tiling(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_colorbar.py`
                                    > *Code Insight:*
                                    ```python
                                    class ColorBar(_BaseTraceHierarchyType):
                                    ```
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pad.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pad(_BaseTraceHierarchyType):
                                    ```
                                📄 `_pattern.py`
                                    > *Code Insight:*
                                    ```python
                                    class Pattern(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **colorbar/**
                                    📄 `_tickfont.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickfont(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_tickformatstop.py`
                                        > *Code Insight:*
                                        ```python
                                        class Tickformatstop(_BaseTraceHierarchyType):
                                        ```
                                    📄 `_title.py`
                                        > *Code Insight:*
                                        ```python
                                        class Title(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                                    📂 **title/**
                                        📄 `_font.py`
                                            > *Code Insight:*
                                            ```python
                                            class Font(_BaseTraceHierarchyType):
                                            ```
                                        📄 `__init__.py`
                                            > *Code Insight:*
                                            ```python
                                            ```
                            📂 **pathbar/**
                                📄 `_textfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Textfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **violin/**
                            📄 `_box.py`
                                > *Code Insight:*
                                ```python
                                class Box(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_line.py`
                                > *Code Insight:*
                                ```python
                                class Line(_BaseTraceHierarchyType):
                                ```
                            📄 `_marker.py`
                                > *Code Insight:*
                                ```python
                                class Marker(_BaseTraceHierarchyType):
                                ```
                            📄 `_meanline.py`
                                > *Code Insight:*
                                ```python
                                class Meanline(_BaseTraceHierarchyType):
                                ```
                            📄 `_selected.py`
                                > *Code Insight:*
                                ```python
                                class Selected(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_unselected.py`
                                > *Code Insight:*
                                ```python
                                class Unselected(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **box/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **marker/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **selected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **unselected/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **volume/**
                            📄 `_caps.py`
                                > *Code Insight:*
                                ```python
                                class Caps(_BaseTraceHierarchyType):
                                ```
                            📄 `_colorbar.py`
                                > *Code Insight:*
                                ```python
                                class ColorBar(_BaseTraceHierarchyType):
                                ```
                            📄 `_contour.py`
                                > *Code Insight:*
                                ```python
                                class Contour(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_lighting.py`
                                > *Code Insight:*
                                ```python
                                class Lighting(_BaseTraceHierarchyType):
                                ```
                            📄 `_lightposition.py`
                                > *Code Insight:*
                                ```python
                                class Lightposition(_BaseTraceHierarchyType):
                                ```
                            📄 `_slices.py`
                                > *Code Insight:*
                                ```python
                                class Slices(_BaseTraceHierarchyType):
                                ```
                            📄 `_spaceframe.py`
                                > *Code Insight:*
                                ```python
                                class Spaceframe(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_surface.py`
                                > *Code Insight:*
                                ```python
                                class Surface(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **caps/**
                                📄 `_x.py`
                                    > *Code Insight:*
                                    ```python
                                    class X(_BaseTraceHierarchyType):
                                    ```
                                📄 `_y.py`
                                    > *Code Insight:*
                                    ```python
                                    class Y(_BaseTraceHierarchyType):
                                    ```
                                📄 `_z.py`
                                    > *Code Insight:*
                                    ```python
                                    class Z(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **colorbar/**
                                📄 `_tickfont.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickfont(_BaseTraceHierarchyType):
                                    ```
                                📄 `_tickformatstop.py`
                                    > *Code Insight:*
                                    ```python
                                    class Tickformatstop(_BaseTraceHierarchyType):
                                    ```
                                📄 `_title.py`
                                    > *Code Insight:*
                                    ```python
                                    class Title(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **title/**
                                    📄 `_font.py`
                                        > *Code Insight:*
                                        ```python
                                        class Font(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **slices/**
                                📄 `_x.py`
                                    > *Code Insight:*
                                    ```python
                                    class X(_BaseTraceHierarchyType):
                                    ```
                                📄 `_y.py`
                                    > *Code Insight:*
                                    ```python
                                    class Y(_BaseTraceHierarchyType):
                                    ```
                                📄 `_z.py`
                                    > *Code Insight:*
                                    ```python
                                    class Z(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **waterfall/**
                            📄 `_connector.py`
                                > *Code Insight:*
                                ```python
                                class Connector(_BaseTraceHierarchyType):
                                ```
                            📄 `_decreasing.py`
                                > *Code Insight:*
                                ```python
                                class Decreasing(_BaseTraceHierarchyType):
                                ```
                            📄 `_hoverlabel.py`
                                > *Code Insight:*
                                ```python
                                class Hoverlabel(_BaseTraceHierarchyType):
                                ```
                            📄 `_increasing.py`
                                > *Code Insight:*
                                ```python
                                class Increasing(_BaseTraceHierarchyType):
                                ```
                            📄 `_insidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Insidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_legendgrouptitle.py`
                                > *Code Insight:*
                                ```python
                                class Legendgrouptitle(_BaseTraceHierarchyType):
                                ```
                            📄 `_outsidetextfont.py`
                                > *Code Insight:*
                                ```python
                                class Outsidetextfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_stream.py`
                                > *Code Insight:*
                                ```python
                                class Stream(_BaseTraceHierarchyType):
                                ```
                            📄 `_textfont.py`
                                > *Code Insight:*
                                ```python
                                class Textfont(_BaseTraceHierarchyType):
                                ```
                            📄 `_totals.py`
                                > *Code Insight:*
                                ```python
                                class Totals(_BaseTraceHierarchyType):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **connector/**
                                📄 `_line.py`
                                    > *Code Insight:*
                                    ```python
                                    class Line(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **decreasing/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **marker/**
                                    📄 `_line.py`
                                        > *Code Insight:*
                                        ```python
                                        class Line(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **hoverlabel/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **increasing/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **marker/**
                                    📄 `_line.py`
                                        > *Code Insight:*
                                        ```python
                                        class Line(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                            📂 **legendgrouptitle/**
                                📄 `_font.py`
                                    > *Code Insight:*
                                    ```python
                                    class Font(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **totals/**
                                📄 `_marker.py`
                                    > *Code Insight:*
                                    ```python
                                    class Marker(_BaseTraceHierarchyType):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                                📂 **marker/**
                                    📄 `_line.py`
                                        > *Code Insight:*
                                        ```python
                                        class Line(_BaseTraceHierarchyType):
                                        ```
                                    📄 `__init__.py`
                                        > *Code Insight:*
                                        ```python
                                        ```
                    📂 **io/**
                        📄 `base_renderers.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `json.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `kaleido.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `orca.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `_base_renderers.py`
                            > *Code Insight:*
                            ```python
                            class BaseRenderer(object):
                            ```
                        📄 `_defaults.py`
                            > *Code Insight:*
                            ```python
                            class _Defaults(object):
                            ```
                        📄 `_html.py`
                            > *Code Insight:*
                            ```python
                            def _generate_sri_hash(content):
                            ```
                        📄 `_json.py`
                            > *Code Insight:*
                            ```python
                            class JsonConfig(object):
                            ```
                        📄 `_kaleido.py`
                            > *Code Insight:*
                            ```python
                            def kaleido_scope_default_warning_func(x):
                            ```
                        📄 `_orca.py`
                            > *Code Insight:*
                            ```python
                            def raise_format_value_error(val):
                            ```
                        📄 `_renderers.py`
                            > *Code Insight:*
                            ```python
                            def display_jupyter_version_warnings():
                            ```
                        📄 `_sg_scraper.py`
                            > *Code Insight:*
                            ```python
                            def plotly_sg_scraper(block, block_vars, gallery_conf, **kwargs):
                            ```
                        📄 `_templates.py`
                            > *Code Insight:*
                            ```python
                            class TemplatesConfig(object):
                            ```
                        📄 `_utils.py`
                            > *Code Insight:*
                            ```python
                            def validate_coerce_fig_to_dict(fig, validate):
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **labextension/**
                        📄 `package.json`
                            > *Code Insight:*
                            ```python
                            ```
                        📂 **static/**
                            📄 `340.c2a5c2a0762f15840a49.js`
                            📄 `remoteEntry.7be085a97cbb02a077cc.js`
                            📄 `style.js`
                    📂 **matplotlylib/**
                        📄 `mpltools.py`
                            > *Code Insight:*
                            ```python
                            def check_bar_match(old_bar, new_bar):
                            ```
                        📄 `renderer.py`
                            > *Code Insight:*
                            ```python
                            def warning_on_one_line(msg, category, filename, lineno, file=None, line=None):
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📂 **mplexporter/**
                            📄 `exporter.py`
                                > *Code Insight:*
                                ```python
                                class Exporter(object):
                                ```
                            📄 `tools.py`
                                > *Code Insight:*
                                ```python
                                def ipynb_vega_init():
                                ```
                            📄 `utils.py`
                                > *Code Insight:*
                                ```python
                                def export_color(color):
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                            📂 **renderers/**
                                📄 `base.py`
                                    > *Code Insight:*
                                    ```python
                                    class Renderer(object):
                                    def ax_zoomable(ax):
                                    ```
                                📄 `fake_renderer.py`
                                    > *Code Insight:*
                                    ```python
                                    class FakeRenderer(Renderer):
                                    ```
                                📄 `vega_renderer.py`
                                    > *Code Insight:*
                                    ```python
                                    class VegaRenderer(Renderer):
                                    def open_figure(self, fig, props):
                                    ```
                                📄 `vincent_renderer.py`
                                    > *Code Insight:*
                                    ```python
                                    class VincentRenderer(Renderer):
                                    def open_figure(self, fig, props):
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                            📂 **tests/**
                                📄 `test_basic.py`
                                    > *Code Insight:*
                                    ```python
                                    def fake_renderer_output(fig, Renderer):
                                    ```
                                📄 `test_utils.py`
                                    > *Code Insight:*
                                    ```python
                                    def test_path_data():
                                    ```
                                📄 `__init__.py`
                                    > *Code Insight:*
                                    ```python
                                    ```
                        📂 **tests/**
                            📄 `test_renderer.py`
                                > *Code Insight:*
                                ```python
                                def test_native_legend_enabled_when_matplotlib_legend_present():
                                ```
                            📄 `__init__.py`
                                > *Code Insight:*
                                ```python
                                ```
                    📂 **offline/**
                        📄 `offline.py`
                            > *Code Insight:*
                            ```python
                            def download_plotlyjs(download_url):
                            ```
                        📄 `_plotlyjs_version.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            ```
                    📂 **package_data/**
                        📄 `plotly.min.js`
                        📄 `widgetbundle.js`
                        📂 **datasets/**
                            📄 `carshare.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `election.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `election.geojson.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `experiment.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `gapminder.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `iris.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `medals.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `stocks.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `tips.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                            📄 `wind.csv.gz`
                                [Error reading file: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte]
                        📂 **templates/**
                            📄 `ggplot2.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `gridon.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `plotly.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `plotly_dark.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `plotly_white.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `presentation.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `seaborn.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `simple_white.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `xgridoff.json`
                                > *Code Insight:*
                                ```python
                                ```
                            📄 `ygridoff.json`
                                > *Code Insight:*
                                ```python
                                ```
                    📂 **validators/**
                        📄 `_validators.json`
                            > *Code Insight:*
                            ```python
                            ```
                📂 **plotly-6.5.0.dist-info/**
                    📄 `entry_points.txt`
                    📄 `INSTALLER`
                    📄 `METADATA`
                    📄 `RECORD`
                    📄 `REQUESTED`
                    📄 `top_level.txt`
                    📄 `WHEEL`
                    📂 **licenses/**
                        📄 `LICENSE.txt`
                📂 **_plotly_utils/**
                    📄 `basevalidators.py`
                        > *Code Insight:*
                        ```python
                        def fullmatch(regex, string, flags=0):
                        ```
                    📄 `data_utils.py`
                        > *Code Insight:*
                        ```python
                        def image_array_to_data_uri(img, backend="pil", compression=4, ext="png"):
                        ```
                    📄 `exceptions.py`
                        > *Code Insight:*
                        ```python
                        class PlotlyError(Exception):
                        ```
                    📄 `files.py`
                        > *Code Insight:*
                        ```python
                        def _permissions():
                        ```
                    📄 `importers.py`
                        > *Code Insight:*
                        ```python
                        def relative_import(parent_name, rel_modules=(), rel_classes=()):
                        ```
                    📄 `optional_imports.py`
                        > *Code Insight:*
                        ```python
                        def get_module(name, should_load=True):
                        ```
                    📄 `png.py`
                        > *Code Insight:*
                        ```python
                        def adam7_generate(width, height):
                        ```
                    📄 `utils.py`
                        > *Code Insight:*
                        ```python
                        def to_typed_array_spec(v):
                        ```
                    📄 `__init__.py`
                        > *Code Insight:*
                        ```python
                        ```
                    📂 **colors/**
                        📄 `carto.py`
                            > *Code Insight:*
                            ```python
                            def swatches(template=None):
                            ```
                        📄 `cmocean.py`
                            > *Code Insight:*
                            ```python
                            def swatches(template=None):
                            ```
                        📄 `colorbrewer.py`
                            > *Code Insight:*
                            ```python
                            def swatches(template=None):
                            ```
                        📄 `cyclical.py`
                            > *Code Insight:*
                            ```python
                            def swatches(template=None):
                            ```
                        📄 `diverging.py`
                            > *Code Insight:*
                            ```python
                            def swatches(template=None):
                            ```
                        📄 `plotlyjs.py`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `qualitative.py`
                            > *Code Insight:*
                            ```python
                            def swatches(template=None):
                            ```
                        📄 `sequential.py`
                            > *Code Insight:*
                            ```python
                            def swatches(template=None):
                            ```
                        📄 `_swatches.py`
                            > *Code Insight:*
                            ```python
                            def _swatches(module_names, module_contents, template=None):
                            ```
                        📄 `__init__.py`
                            > *Code Insight:*
                            ```python
                            def color_parser(colors, function):
                            ```
        📂 **Scripts/**
            📄 `activate`
            📄 `activate.bat`
            📄 `Activate.ps1`
            📄 `deactivate.bat`
            📄 `pip.exe`
                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
            📄 `pip3.12.exe`
                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
            📄 `pip3.exe`
                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
            📄 `plotly_get_chrome.exe`
                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
            📄 `python.exe`
                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
            📄 `pythonw.exe`
                [Error reading file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
        📂 **share/**
            📂 **jupyter/**
                📂 **labextensions/**
                    📂 **jupyterlab-plotly/**
                        📄 `install.json`
                            > *Code Insight:*
                            ```python
                            ```
                        📄 `package.json`
                            > *Code Insight:*
                            ```python
                            ```
                        📂 **static/**
                            📄 `340.c2a5c2a0762f15840a49.js`
                            📄 `remoteEntry.7be085a97cbb02a077cc.js`
                            📄 `style.js`
    📂 **catalogue/**
        📄 `Agent_Base.py`
            > *Code Insight:*
            ```python
            BASE CLASS: Agent_Base
            ```
        📄 `agent_catalogue.py`
            > *Code Insight:*
            ```python
            Agent Catalogue for MAaaS
            ```
        📄 `agent_Compliance.py`
            > *Code Insight:*
            ```python
            class Agent_Compliance:
            BASE CLASS: Agent_Compliance
            ```
        📄 `Agent_DBA.py`
            > *Code Insight:*
            ```python
            BASE CLASS: Agent_DBA (Database Architect)
            ```
        📄 `agent_Dev_Backend.py`
            > *Code Insight:*
            ```python
            class Agent_Dev_Backend:
            BASE CLASS: Agent_Dev_Backend
            ```
        📄 `Agent_Expertise.py`
            > *Code Insight:*
            ```python
            This module implements the "Agentic Expertise" pattern where agents maintain
            ```
        📄 `agent_FinancialOfficer.py`
            > *Code Insight:*
            ```python
            class Agent_FinancialOfficer:
            BASE CLASS: Agent_FinancialOfficer
            ```
        📄 `Agent_Marketer.py`
            > *Code Insight:*
            ```python
            BASE CLASS: Agent_Marketer (Growth Officer)
            ```
        📄 `Agent_NetSec.py`
            > *Code Insight:*
            ```python
            BASE CLASS: Agent_NetSec (Network Security Sentinel)
            ```
        📄 `agent_Researcher.py`
            > *Code Insight:*
            ```python
            class Agent_Researcher:
            BASE CLASS: Agent_Researcher
            ```
        📄 `gent_ProjectManager.py`
            > *Code Insight:*
            ```python
            from catalogue.Agent_Base import Agent_Base
            ```
        📄 `MCP_USAGE_EXAMPLE.md`
            > *Code Insight:*
            ```python
            # MCP Usage Example for Agents
            ```
    📂 **docs/**
        📄 `SLA_Maintenance_Protocol.md`
            > *Code Insight:*
            ```python
            ## MAaaS Platform - Multi-Agent as a Service
            ```
    📂 **intake/**
        📄 `marketing_test_profile.json`
            > *Code Insight:*
            ```python
            ```
    📂 **tools/**
        📄 `mcp_market_scanner.py`
            > *Code Insight:*
            ```python
            class MarketScannerTool:
            Standardizes the search logic so Agents can invoke it autonomously
            ```
        📄 `README.md`
            > *Code Insight:*
            ```python
            ## Agent Code Mode Usage
            ```
        📄 `Universal_MCP_Client.py`
            > *Code Insight:*
            ```python
            class TransportType(Enum):
            ```
        📄 `__init__.py`
            > *Code Insight:*
            ```python
            ```
