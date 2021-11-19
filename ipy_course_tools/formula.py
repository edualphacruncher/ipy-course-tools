from sympy.interactive import printing
from sympy import Matrix, MatrixSymbol, Symbol
from IPython.display import Math
import itertools


def show_matrix(symbol, matrix, formula_op="=", formula_align=False, display=False):

    if formula_align:
        op = f"&{formula_op}"
    else:
        op = f"{formula_op}"

    ret_text = f"{symbol} {op} {printing.default_latex(matrix)}"

    if not display:
        return ret_text
    else:
        return Math(ret_text)


def eval_formula(formula, display=False):

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
                ret_text = f"{eval_formula(formula)} {op}"
        else:
            if formula_suffix:
                ret_text = f"{op} {formula}" + ret_text
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
                ret_text = f"{eval_formula(formula)} {op}"
        else:
            if formula_suffix:
                ret_text += f"{op} {formula}" + ret_text
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
                ret_text = f"{eval_formula(formula)} {op}"
        else:  # we got latex formula
            if formula_suffix:
                ret_text = f"{op} {formula}" + ret_text
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
