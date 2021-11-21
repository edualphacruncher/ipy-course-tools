from sympy.interactive import printing
from sympy import Matrix, MatrixSymbol, Symbol, poly
from sympy.abc import x
from IPython.display import Math
import itertools


def show_formula(symbol, value, formula_op="=", formula_align=False, display=False):
    """Pretty print a sympy formula. This embeds the formula expression a LaTeX equation with a proper LHS, making it possible to name matrices, expressions in output, etc.

    Args:
        symbol (string): A standard LaTeX string you would like to be on the LHS of a pretty print.
        matrix (sympy.Matrix): The sympy Matrix object you would like to pretty print.
        formula_op (str, optional): LaTeX operator symbol. Defaults to "=".
        formula_align (bool, optional): Whether to add a '&' character for including in align LaTeX environments to the operator symbol. Defaults to False.
        display (bool, optional): If False, returns LaTeX string output. If True, returns Math rendering of LaTeX string. Defaults to False.

    Returns:
        [str or Math render]: Either LaTeX string or IPython rendering thereof.
    """
    if formula_align:
        op = f"&{formula_op}"
    else:
        op = f"{formula_op}"

    ret_text = f"{symbol} {op} {printing.default_latex(value)}"

    if not display:
        return ret_text
    else:
        return Math(ret_text)


def show_matrix(symbol, matrix, formula_op="=", formula_align=False, display=False):
    """Pretty print a sympy matrix object. This embeds the Matrix render into a LaTeX equation with a proper LHS, making it possible to name matrices in output, etc.

    Args:
        symbol (string): A standard LaTeX string you would like to be on the LHS of a pretty print.
        matrix (sympy.Matrix): The sympy Matrix object you would like to pretty print.
        formula_op (str, optional): LaTeX operator symbol. Defaults to "=".
        formula_align (bool, optional): Whether to add a '&' character for including in align LaTeX environments to the operator symbol. Defaults to False.
        display (bool, optional): If False, returns LaTeX string output. If True, returns Math rendering of LaTeX string. Defaults to False.

    Returns:
        [str or Math render]: Either LaTeX string or IPython rendering thereof.
    """
    return show_formula(
        symbol=symbol,
        value=matrix,
        formula_op=formula_op,
        formula_align=formula_align,
        display=display,
    )


def eval_formula(formula, display=False):
    """Pretty print generic sympy formulaic expression.

    Args:
        formula (sympy expression): Sympy expression to render.
        display (bool, optional): If False, returns LaTeX string output. If True, returns Math rendering of LaTeX string. Defaults to False.

    Returns:
        [str or Math render]: Either LaTeX string or IPython rendering thereof.
    """
    ret_text = printing.default_latex(formula)
    if not display:
        return ret_text
    else:
        return Math(ret_text)


def unary_bracket(
    x,
    formula=None,
    lbracket_string="(",
    rbracket_string=")",
    formula_op="=",
    formula_align=False,
    subscript=None,
    display=False,
    x_latex=False,
    formula_latex=False,
    formula_suffix=True,
):
    """Internal function to pretty print all unary bracketed formulae with sympy. In particular norms, absolute values, etc. can be printed with this.

    Args:
        x (string or sympy expression): Content of unary symbol you want to pretty print.
        formula (sypmpy expression or LaTeX string, optional): Additional artifacts you want to render along your unary. Either "evaluates to" or "is equal to" would be good ways to interpret what to put here. Defaults to None.
        lbracket_string (str, optional): LaTeX bracket type on the left hand side of the unary. Defaults to "(".
        rbracket_string (str, optional): LaTeX bracket type on the right hand side of the unary. Defaults to ")".
        formula_op (str, optional): If there is a formula, what should be the operator that separates the formula from the unary? Defaults to "=".
        formula_align (bool, optional): Whether to add a '&' character for including in align LaTeX environments to the operator symbol. Defaults to False.
        subscript ([type], optional): Add a subscript to the right hand bracket if not None. Defaults to None.
        display (bool, optional): If False, returns LaTeX string output. If True, returns Math rendering of LaTeX string. Defaults to False.
        x_latex (bool, optional): Whether the content of the unary is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_latex (bool, optional): Whether the content of the formula is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_suffix (bool, optional): Whether formula comes first (False) or the unary (True). Defaults to True.

    Returns:
        [str or Math render]: Either LaTeX string or IPython rendering thereof.
    """
    if not x_latex:
        x_text = printing.default_latex(x)
    else:
        x_text = x

    if subscript is None:
        ret_text = f"\left{lbracket_string} {x_text} \\right{rbracket_string} "
    else:
        ret_text = (
            f"\left{lbracket_string} {x_text} \\right{rbracket_string}_{subscript}"
        )

    if formula_align:
        op = f"&{formula_op}"
    else:
        op = f"{formula_op}"

    if formula is not None:
        if not formula_latex:
            if formula_suffix:
                ret_text += f"{op} {eval_formula(formula)}"
            else:
                ret_text = f"{eval_formula(formula)} {op}" + ret_text
        else:
            if formula_suffix:
                ret_text += f"{op} {formula}"
            else:
                ret_text = f"{formula} {op}" + ret_text

    if not display:
        return ret_text
    else:
        return Math(ret_text)


def binary_bracket(
    x,
    y,
    formula=None,
    lbracket_string="(",
    rbracket_string=")",
    formula_op="=",
    formula_align=False,
    subscript=None,
    display=False,
    x_latex=False,
    y_latex=False,
    formula_latex=False,
    formula_suffix=True,
):
    """Internal function to pretty print all binary bracketed formulae with sympy. In particular scalar products, etc. can be printed with this.

    Args:
        x (string or sympy expression): Content of binary symbol you want to pretty print, left expression.
        y (string or sympy expression): Content of binary symbol you want to pretty print, right expression.
        formula (sypmpy expression or LaTeX string, optional): Additional artifacts you want to render along your unary. Either "evaluates to" or "is equal to" would be good ways to interpret what to put here. Defaults to None.
        lbracket_string (str, optional): LaTeX bracket type on the left hand side of the unary. Defaults to "(".
        rbracket_string (str, optional): LaTeX bracket type on the right hand side of the unary. Defaults to ")".
        formula_op (str, optional): If there is a formula, what should be the operator that separates the formula from the unary? Defaults to "=".
        formula_align (bool, optional): Whether to add a '&' character for including in align LaTeX environments to the operator symbol. Defaults to False.
        subscript ([type], optional): Add a subscript to the right hand bracket if not None. Defaults to None.
        display (bool, optional): If False, returns LaTeX string output. If True, returns Math rendering of LaTeX string. Defaults to False.
        x_latex (bool, optional): Whether the content of the binary left is LaTeX (True) or Sympy Expression (False). Defaults to False.
        y_latex (bool, optional): Whether the content of the binary right is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_latex (bool, optional): Whether the content of the formula is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_suffix (bool, optional): Whether formula comes first (False) or the binary (True). Defaults to True.

    Returns:
        [str or Math render]: Either LaTeX string or IPython rendering thereof.
    """
    if not x_latex:
        x_text = printing.default_latex(x)
    else:
        x_text = x

    if not y_latex:
        y_text = printing.default_latex(y)
    else:
        y_text = y

    if subscript is None:
        ret_text = (
            f"\left{lbracket_string} {x_text} , {y_text}  \\right{rbracket_string} "
        )
    else:
        ret_text = f"\left{lbracket_string} {x_text} , {y_text}  \\right{rbracket_string}_{subscript}"

    if formula_align:
        op = f"&{formula_op}"
    else:
        op = f"{formula_op}"

    if formula is not None:
        if not formula_latex:
            if formula_suffix:
                ret_text += f"{op} {eval_formula(formula)}"
            else:
                ret_text = f"{eval_formula(formula)} {op}" + ret_text
        else:
            if formula_suffix:
                ret_text += f"{op} {formula}"
            else:
                ret_text = f"{formula} {op}" + ret_text

    if not display:
        return ret_text
    else:
        return Math(ret_text)


def n_ary_bracket(
    items,
    formula=None,
    prefix=None,
    lbracket_string="(",
    rbracket_string=")",
    formula_op="=",
    formula_align=False,
    subscript=None,
    display=False,
    items_latex=False,
    formula_latex=False,
    formula_suffix=True,
):
    """Internal function to pretty print all n-ary bracketed formulae with sympy. In particular vector systems, convex hulls, etc. can be printed with this.

    Args:
        items (list of strings or sympy expressions, has to be uniform): Content of n-ary symbol you want to pretty print, left expression.
        formula (sypmpy expression or LaTeX string, optional): Additional artifacts you want to render along your unary. Either "evaluates to" or "is equal to" would be good ways to interpret what to put here. Defaults to None.
        lbracket_string (str, optional): LaTeX bracket type on the left hand side of the unary. Defaults to "(".
        rbracket_string (str, optional): LaTeX bracket type on the right hand side of the unary. Defaults to ")".
        formula_op (str, optional): If there is a formula, what should be the operator that separates the formula from the unary? Defaults to "=".
        formula_align (bool, optional): Whether to add a '&' character for including in align LaTeX environments to the operator symbol. Defaults to False.
        subscript ([type], optional): Add a subscript to the right hand bracket if not None. Defaults to None.
        display (bool, optional): If False, returns LaTeX string output. If True, returns Math rendering of LaTeX string. Defaults to False.
        items_latex (bool, optional): Whether the content of the n-ary is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_latex (bool, optional): Whether the content of the formula is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_suffix (bool, optional): Whether formula comes first (False) or the n-ary (True). Defaults to True.

    Returns:
        [str or Math render]: Either LaTeX string or IPython rendering thereof.
    """
    if len(items) < 1:
        print("No items received, not printing anything.")
        return

    if not items_latex:
        items_text = [eval_formula(x) for x in items]
    else:
        items_text = items

    # Setting up what's going to be inside the brackets

    term_count = len(items)
    base_string = "{}"
    for i in range(1, term_count):
        base_string += ", {} "

    in_brackets = base_string.format(*items_text)

    if subscript is None:
        ret_text = "{}\left{} {} \\right{} ".format(
            prefix, lbracket_string, in_brackets, rbracket_string
        )
    else:
        ret_text = "\left{} {} \\right{}_{}".format(
            prefix, lbracket_string, in_brackets, rbracket_string, subscript
        )

    if formula_align:
        op = f"&{formula_op}"
    else:
        op = f"{formula_op}"

    if formula is not None:
        if not formula_latex:
            if formula_suffix:
                ret_text += f"{op} {eval_formula(formula)}"
            else:
                ret_text = f"{eval_formula(formula)} {op}" + ret_text
        else:  # we got latex formula
            if formula_suffix:
                ret_text += f"{op} {formula}"
            else:
                ret_text = f"{formula} {op}" + ret_text

    if not display:
        return ret_text
    else:
        return Math(ret_text)


def scalar_product(
    x,
    y,
    formula=None,
    formula_op="=",
    formula_align=False,
    subscript=None,
    display=False,
    x_latex=False,
    y_latex=False,
    formula_latex=False,
):
    """Pretty print scalar products of the form <x,y>. Special case of binary_bracket with \langle and \\rangle.

    Args:
        x (string or sympy expression): Content of left element you want to pretty print.
        y (string or sympy expression): Content of right element you want to pretty print.
        formula (sypmpy expression or LaTeX string, optional): Additional artifacts you want to render along your unary. Either "evaluates to" or "is equal to" would be good ways to interpret what to put here. Defaults to None.
        formula_op (str, optional): If there is a formula, what should be the operator that separates the formula from the unary? Defaults to "=".
        formula_align (bool, optional): Whether to add a '&' character for including in align LaTeX environments to the operator symbol. Defaults to False.
        subscript ([type], optional): Add a subscript to the right hand bracket if not None. Defaults to None.
        display (bool, optional): If False, returns LaTeX string output. If True, returns Math rendering of LaTeX string. Defaults to False.
        x_latex (bool, optional): Whether the content of the left element is LaTeX (True) or Sympy Expression (False). Defaults to False.
        y_latex (bool, optional): Whether the content of the right element is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_latex (bool, optional): Whether the content of the formula is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_suffix (bool, optional): Whether formula comes first (False) or the scalar product (True). Defaults to True.

    Returns:
        [str or Math render]: Either LaTeX string or IPython rendering thereof.
    """
    return binary_bracket(
        x,
        y,
        formula=formula,
        lbracket_string="\\langle",
        rbracket_string="\\rangle",
        formula_op=formula_op,
        formula_align=formula_align,
        subscript=subscript,
        display=display,
        x_latex=x_latex,
        y_latex=y_latex,
        formula_latex=formula_latex,
    )


def norm(
    x,
    formula=None,
    formula_op="=",
    formula_align=False,
    subscript=None,
    display=False,
    x_latex=False,
    formula_latex=False,
):
    """Pretty print norms of the form |x|. Special case of unary_bracket with \|.\|.

    Args:
        x (string or sympy expression): Content of the norm you want to pretty print.
        formula (sypmpy expression or LaTeX string, optional): Additional artifacts you want to render along your norm. Either "evaluates to" or "is equal to" would be good ways to interpret what to put here. Defaults to None.
        formula_op (str, optional): If there is a formula, what should be the operator that separates the formula from the norm? Defaults to "=".
        formula_align (bool, optional): Whether to add a '&' character for including in align LaTeX environments to the operator symbol. Defaults to False.
        subscript ([type], optional): Add a subscript to the right hand bracket if not None. Defaults to None.
        display (bool, optional): If False, returns LaTeX string output. If True, returns Math rendering of LaTeX string. Defaults to False.
        x_latex (bool, optional): Whether the content of the norm is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_latex (bool, optional): Whether the content of the formula is LaTeX (True) or Sympy Expression (False). Defaults to False.
        formula_suffix (bool, optional): Whether formula comes first (False) or the norm (True). Defaults to True.

    Returns:
        [str or Math render]: Either LaTeX string or IPython rendering thereof.
    """
    return unary_bracket(
        x,
        formula=formula,
        lbracket_string="\|",
        rbracket_string="\|",
        formula_op=formula_op,
        formula_align=formula_align,
        subscript=subscript,
        display=display,
        x_latex=x_latex,
        formula_latex=formula_latex,
    )


def eqn_align(eqn_list, display=False):
    """Equation array pretty printing. Requires a list of pre-pared LaTeX strings which are then substituted to an appropriately sized align LaTeX environment. Please make sure that all item elements were generated with alignment characters (c.f. formula_align parameters of bracketed expressions).

    Args:
        eqn_list ([type]): [description]
        display (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    """
    if len(eqn_list) < 1:
        print("No equations received, not printing anything.")
        return

    eqn_count = len(eqn_list)

    base_string = "{}"
    for i in range(1, eqn_count):
        base_string = base_string + "\\\ {}"
    start = "\\begin{{align}} "
    end = " \\end{{align}}"
    full_string = start + base_string + end
    eqnarray_string = full_string.format(*eqn_list)
    if not display:
        return eqnarray_string
    return Math(eqnarray_string)


def linear_combination(
    coefs,
    vectors,
    formula,
    formula_op="=",
    formula_align=False,
    display=False,
    coef_latex=False,
    vector_latex=False,
    formula_latex=False,
    formula_suffix=True,
):
    if len(coefs) < 1 or len(vectors) < 1:
        print("No coefs or vectors received, not printing anything.")
        return
    if len(coefs) != len(vectors):
        print(
            "The number of coefficients and vectors do not agree. Please provide an equal number of coefficients and vectors."
        )
        return

    term_count = len(coefs)
    base_string = "{} \\cdot {}"

    for i in range(1, term_count):
        base_string += "+ {} \\cdot {}"

    if not coef_latex:
        coefs_interpret = [eval_formula(x) for x in coefs]
    else:
        coefs_interpret = coefs

    if not vector_latex:
        vectors_interpret = [eval_formula(x) for x in vectors]
    else:
        vectors_interpret = vectors

        # merge the coef and vector arrays alternatingly
    sub_list = [
        x
        for x in itertools.chain.from_iterable(
            itertools.zip_longest(coefs_interpret, vectors_interpret)
        )
        if x
    ]

    if formula_align:
        op = "&{}".format(formula_op)
    else:
        op = "{}".format(formula_op)

    if formula is not None:
        if not formula_latex:
            if formula_suffix:
                base_string += "{} {}"
                sub_list += [op, eval_formula(formula)]
            else:
                base_string = "{} {}" + base_string
                sub_list = [eval_formula(formula), op] + sub_list
        else:
            if formula_suffix:
                base_string += "{} {}"
                sub_list += [op, formula]
            else:
                base_string = "{} {}" + base_string
                sub_list = [formula, op] + sub_list

    sub_list = [x for x in sub_list]

    comb_string = base_string.format(*sub_list)

    if not display:
        return comb_string
    return Math(comb_string)


def linear_hull(
    items,
    formula=None,
    formula_op="=",
    formula_align=False,
    subscript=None,
    display=False,
    items_latex=False,
    formula_latex=False,
    formula_suffix=True,
):

    return n_ary_bracket(
        items,
        formula=formula,
        prefix="\\text{lin}",
        lbracket_string="(",
        rbracket_string=")",
        formula_op=formula_op,
        formula_align=formula_align,
        subscript=subscript,
        display=display,
        items_latex=items_latex,
        formula_latex=formula_latex,
        formula_suffix=formula_suffix,
    )


def convex_hull(
    items,
    formula=None,
    formula_op="=",
    formula_align=False,
    subscript=None,
    display=False,
    items_latex=False,
    formula_latex=False,
    formula_suffix=True,
):

    return n_ary_bracket(
        items,
        formula=formula,
        prefix="\\text{co}",
        lbracket_string="(",
        rbracket_string=")",
        formula_op=formula_op,
        formula_align=formula_align,
        subscript=subscript,
        display=display,
        items_latex=items_latex,
        formula_latex=formula_latex,
        formula_suffix=formula_suffix,
    )


def affine_hull(
    items,
    formula=None,
    formula_op="=",
    formula_align=False,
    subscript=None,
    display=False,
    items_latex=False,
    formula_latex=False,
    formula_suffix=True,
):

    return n_ary_bracket(
        items,
        formula=formula,
        prefix="\\text{aff}",
        lbracket_string="(",
        rbracket_string=")",
        formula_op=formula_op,
        formula_align=formula_align,
        subscript=subscript,
        display=display,
        items_latex=items_latex,
        formula_latex=formula_latex,
        formula_suffix=formula_suffix,
    )


def generate_parametric_poly(degree, symbol="x", coef="a", domain="ZZ", display=True):
    from sympy import parse_expr

    coefs = [Symbol(f"a_{i}", real=True) for i in range(0, degree)]
    expr = ""
    for i in range(0, degree):
        expr += f"+ {coefs[i]}*{symbol}**{i}"
    return parse_expr(expr)
