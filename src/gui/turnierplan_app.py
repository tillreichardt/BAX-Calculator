"""Lokales Turnierplan-GUI (tkinter): Ausgangslage, Turniere, Simulation — Dark UI."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Optional, Tuple

from src.berechnung.turnier_simulation import (
    SimulationResult,
    calc_bneu,
    gew,
    recommendation_text,
    simulate_from_base,
)


FIELD_PRESETS = [
    ("C-Feld (Ø420)", 420),
    ("B-Feld (Ø470)", 470),
    ("A-Feld (Ø520)", 520),
]

# Palette (aligned with reference mockups)
BG = "#121212"
BG_CARD = "#222222"
BG_ROW = "#252525"
FG = "#ffffff"
FG_MUTED = "#a0a0a0"
FG_DIM = "#6e7681"
ACCENT_BLUE = "#58a6ff"
ACCENT_GREEN = "#3fb950"
ACCENT_YELLOW = "#facc15"
ACCENT_RED = "#f85149"
BORDER = "#404040"
CHART_BG = "#1c1c1c"


def _field_desc(avg: float, n: int, losses: int) -> str:
    return f"~{avg:.0f} Ø, {n} Spiele, {losses} Niederlage{'n' if losses != 1 else ''} erwartet"


def _bax_row_color(bneu: float) -> str:
    if bneu >= 480:
        return ACCENT_GREEN
    if bneu >= 460:
        return ACCENT_YELLOW
    return FG


class OpponentRow:
    def __init__(
        self,
        parent: tk.Frame,
        on_change: Callable[[], None],
        remove_cb: Callable[["OpponentRow"], None],
    ):
        self._remove_cb = remove_cb
        self.frame = tk.Frame(parent, bg=BG_ROW)
        self.vorname = tk.StringVar()
        self.nachname = tk.StringVar()
        self.verein = tk.StringVar()
        self.ergebnis = tk.StringVar(value="Sieg")

        ttk.Entry(self.frame, textvariable=self.vorname, width=11).grid(row=0, column=0, padx=2, pady=2)
        ttk.Entry(self.frame, textvariable=self.nachname, width=11).grid(row=0, column=1, padx=2, pady=2)
        ttk.Entry(self.frame, textvariable=self.verein, width=12).grid(row=0, column=2, padx=2, pady=2)
        cb = ttk.Combobox(
            self.frame,
            textvariable=self.ergebnis,
            values=("Sieg", "Niederlage"),
            width=9,
            state="readonly",
        )
        cb.grid(row=0, column=3, padx=2, pady=2)
        ttk.Button(self.frame, text="×", width=2, command=self._remove).grid(row=0, column=4, padx=2)
        for v in (self.vorname, self.nachname, self.verein):
            v.trace_add("write", lambda *_: on_change())
        self.ergebnis.trace_add("write", lambda *_: on_change())

    def _remove(self) -> None:
        self._remove_cb(self)

    def destroy(self) -> None:
        self.frame.destroy()


class TournamentBlock:
    def __init__(
        self,
        parent: tk.Frame,
        index: int,
        on_change: Callable[[], None],
        remove_cb: Callable[["TournamentBlock"], None],
    ):
        self.on_change = on_change
        self._remove_cb = remove_cb
        self._index = index

        self.outer = tk.Frame(parent, bg=BG_ROW, highlightbackground=BORDER, highlightthickness=1)
        self.outer.columnconfigure(1, weight=1)

        self.idx_lbl = tk.Label(
            self.outer,
            text=str(index + 1),
            width=2,
            bg=BG_ROW,
            fg=FG_MUTED,
            font=("SF Pro Text", 11),
        )
        self.idx_lbl.grid(row=0, column=0, padx=(10, 6), pady=10, sticky="n")

        title_col = tk.Frame(self.outer, bg=BG_ROW)
        title_col.grid(row=0, column=1, sticky="nw", pady=10)
        self.name_var = tk.StringVar(value="Turnier")
        self.name_entry = ttk.Entry(title_col, textvariable=self.name_var, width=22)
        self.name_entry.pack(anchor="w")
        self.subtitle_lbl = tk.Label(
            title_col,
            text="",
            bg=BG_ROW,
            fg=FG_MUTED,
            font=("SF Pro Text", 9),
        )
        self.subtitle_lbl.pack(anchor="w", pady=(4, 0))

        ctrl = tk.Frame(self.outer, bg=BG_ROW)
        ctrl.grid(row=0, column=2, padx=8, pady=10, sticky="nw")

        self.preset_var = tk.StringVar(value="B-Feld (Ø470)")
        self.preset_cb = ttk.Combobox(
            ctrl,
            textvariable=self.preset_var,
            values=[p[0] for p in FIELD_PRESETS],
            width=18,
            state="readonly",
        )
        self.preset_cb.pack(anchor="w")
        self.preset_cb.bind("<<ComboboxSelected>>", lambda e: (self._apply_preset(), self._update_subtitle(), on_change()))

        spin_fr = tk.Frame(ctrl, bg=BG_ROW)
        spin_fr.pack(anchor="w", pady=(6, 0))
        tk.Label(spin_fr, text="oder Ø", bg=BG_ROW, fg=FG_MUTED, font=("SF Pro Text", 9)).pack(side="left")
        self.custom_avg = tk.IntVar(value=470)
        ttk.Spinbox(spin_fr, from_=300, to=650, textvariable=self.custom_avg, width=6).pack(side="left", padx=4)
        self.custom_avg.trace_add("write", lambda *_: (self._update_subtitle(), on_change()))

        res_fr = tk.Frame(self.outer, bg=BG_ROW)
        res_fr.grid(row=0, column=3, padx=8, pady=10, sticky="nw")
        self.mode = tk.StringVar(value="avg")
        self.avg_fr = tk.Frame(res_fr, bg=BG_ROW)
        self.avg_fr.pack(anchor="w")
        r1 = tk.Frame(self.avg_fr, bg=BG_ROW)
        r1.pack(anchor="w")
        tk.Label(r1, text="Siege:", bg=BG_ROW, fg=FG_MUTED, font=("SF Pro Text", 9)).pack(side="left")
        self.wins_var = tk.IntVar(value=4)
        ttk.Spinbox(r1, from_=0, to=99, textvariable=self.wins_var, width=4).pack(side="left", padx=(4, 8))
        tk.Label(r1, text="Nied.:", bg=BG_ROW, fg=FG_MUTED, font=("SF Pro Text", 9)).pack(side="left")
        self.losses_var = tk.IntVar(value=1)
        ttk.Spinbox(r1, from_=0, to=99, textvariable=self.losses_var, width=4).pack(side="left", padx=4)
        for v in (self.wins_var, self.losses_var):
            v.trace_add("write", lambda *_: (self._update_subtitle(), on_change()))

        mode_fr = tk.Frame(res_fr, bg=BG_ROW)
        mode_fr.pack(anchor="w", pady=(8, 0))
        ttk.Radiobutton(
            mode_fr,
            text="Ø / Siege",
            variable=self.mode,
            value="avg",
            command=self._on_mode_change,
        ).pack(anchor="w")
        ttk.Radiobutton(
            mode_fr,
            text="Gegnerliste",
            variable=self.mode,
            value="opp",
            command=self._on_mode_change,
        ).pack(anchor="w")

        self.opp_fr = tk.Frame(self.outer, bg=BG_ROW)
        hdr = tk.Frame(self.opp_fr, bg=BG_ROW)
        hdr.pack(anchor="w")
        for c, t in enumerate(("Vorname", "Nachname", "Verein", "Ergebnis")):
            tk.Label(hdr, text=t, bg=BG_ROW, fg=FG_MUTED, font=("SF Pro Text", 9, "bold")).grid(
                row=0, column=c, padx=2
            )
        self.opp_inner = tk.Frame(self.opp_fr, bg=BG_ROW)
        self.opp_inner.pack(anchor="w", fill="x")
        self.opponent_rows: List[OpponentRow] = []
        ttk.Button(self.opp_fr, text="Gegner hinzufügen", command=self._add_opponent).pack(anchor="w", pady=4)

        bax_fr = tk.Frame(self.outer, bg=BG_ROW)
        bax_fr.grid(row=0, column=4, padx=(12, 14), pady=10, sticky="ne")
        self.lbl_bax = tk.Label(
            bax_fr,
            text="—",
            bg=BG_ROW,
            fg=ACCENT_GREEN,
            font=("SF Pro Text", 22, "bold"),
        )
        self.lbl_bax.pack(anchor="e")
        self.lbl_delta = tk.Label(
            bax_fr,
            text="",
            bg=BG_ROW,
            fg=ACCENT_GREEN,
            font=("SF Pro Text", 11, "bold"),
        )
        self.lbl_delta.pack(anchor="e")

        head_r = tk.Frame(self.outer, bg=BG_ROW)
        head_r.grid(row=0, column=5, padx=(0, 8), pady=10, sticky="ne")
        ttk.Button(head_r, text="Entfernen", command=lambda: remove_cb(self)).pack(anchor="e")

        self.name_var.trace_add("write", lambda *_: on_change())
        self._add_opponent()
        self._apply_preset()
        self._on_mode_change()
        self._update_subtitle()

    def set_index(self, i: int) -> None:
        self._index = i
        self.idx_lbl.configure(text=str(i + 1))

    def _apply_preset(self) -> None:
        for label, val in FIELD_PRESETS:
            if label == self.preset_var.get():
                self.custom_avg.set(val)
                break

    def _current_avg_bax(self) -> int:
        try:
            return int(self.custom_avg.get())
        except (tk.TclError, ValueError):
            return 420

    def _update_subtitle(self) -> None:
        avg = float(self._current_avg_bax())
        if self.mode.get() == "avg":
            try:
                w = int(self.wins_var.get())
                l = int(self.losses_var.get())
            except (tk.TclError, ValueError):
                return
            n = w + l
            if n == 0:
                self.subtitle_lbl.configure(text="")
                return
            self.subtitle_lbl.configure(text=_field_desc(avg, n, l))
        else:
            n = len(self.opponent_rows)
            wins = sum(1 for r in self.opponent_rows if r.ergebnis.get() == "Sieg")
            losses = n - wins
            if n == 0:
                self.subtitle_lbl.configure(text="")
                return
            self.subtitle_lbl.configure(text=_field_desc(avg, n, losses))

    def set_row_bax(self, bax: Optional[float], delta: Optional[float]) -> None:
        if bax is None:
            self.lbl_bax.configure(text="—", fg=FG_MUTED)
            self.lbl_delta.configure(text="", fg=FG_MUTED)
            return
        col = _bax_row_color(bax)
        self.lbl_bax.configure(text=f"{bax:.0f}", fg=col)
        if delta is not None:
            ds = f"{delta:+.0f}"
            self.lbl_delta.configure(text=ds, fg=col)
        else:
            self.lbl_delta.configure(text="", fg=col)

    def _add_opponent(self) -> None:
        row = OpponentRow(self.opp_inner, self.on_change, self._remove_opponent_row)
        row.frame.pack(fill="x", pady=1)
        self.opponent_rows.append(row)
        self._update_subtitle()
        self.on_change()

    def _on_mode_change(self) -> None:
        if self.mode.get() == "avg":
            self.avg_fr.pack(anchor="w")
            self.opp_fr.grid_remove()
        else:
            self.avg_fr.pack_forget()
            self.opp_fr.grid(row=1, column=1, columnspan=3, sticky="ew", padx=(0, 8), pady=(0, 8))
        self._update_subtitle()
        self.on_change()

    def _remove_opponent_row(self, row: OpponentRow) -> None:
        if len(self.opponent_rows) <= 1:
            return
        self.opponent_rows.remove(row)
        row.destroy()
        self._update_subtitle()
        self.on_change()

    def destroy(self) -> None:
        self.outer.destroy()

    def build_step(self) -> Optional[tuple]:
        name = self.name_var.get().strip() or "Turnier"
        avg = float(self._current_avg_bax())
        if self.mode.get() == "avg":
            try:
                w = int(self.wins_var.get())
                l = int(self.losses_var.get())
            except (tk.TclError, ValueError):
                return None
            n = w + l
            if n == 0:
                return None
            return (name, n, avg, w)
        wins = sum(1 for r in self.opponent_rows if r.ergebnis.get() == "Sieg")
        n = len(self.opponent_rows)
        return (name, n, avg, wins)


class TurnierplanApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("BAX Turnierplan")
        self.root.minsize(860, 620)
        self.root.configure(bg=BG)

        self.balt = tk.IntVar(value=435)
        self.n0 = tk.IntVar(value=30)
        self.bniv0 = tk.IntVar(value=444)
        self.sist0 = tk.StringVar(value="18.0")

        self.tournaments: List[TournamentBlock] = []

        self._recalc_after_id: Optional[str] = None
        self._debounce_ms = 75
        self._summary_metrics_built = False
        self._last_chart_key: Optional[Tuple[float, ...]] = None
        self._last_chart_wh: Tuple[int, int] = (0, 0)

        self._setup_styles()
        self._build_ui()
        if self._recalc_after_id is not None:
            self.root.after_cancel(self._recalc_after_id)
            self._recalc_after_id = None
        self._recalc_impl()

    def _setup_styles(self) -> None:
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", background=BG, foreground=FG, fieldbackground=BG_CARD, darkcolor=BG, lightcolor=BG)
        style.configure("TFrame", background=BG)
        style.configure("Card.TFrame", background=BG_CARD)
        style.configure("TLabel", background=BG, foreground=FG)
        style.configure("Muted.TLabel", background=BG, foreground=FG_MUTED, font=("SF Pro Text", 10))
        style.configure("Title.TLabel", background=BG_CARD, foreground=FG_MUTED, font=("SF Pro Text", 9))
        style.configure("TLabelframe", background=BG_CARD, foreground=FG)
        style.configure("TLabelframe.Label", background=BG_CARD, foreground=FG_MUTED, font=("SF Pro Text", 9))
        style.configure("TButton", background="#2d333b", foreground=FG, borderwidth=0, focusthickness=0)
        style.map("TButton", background=[("active", "#3d444d")])
        style.configure("TEntry", fieldbackground=BG_ROW, foreground=FG, bordercolor=BORDER)
        style.configure("TSpinbox", fieldbackground=BG_ROW, foreground=FG, bordercolor=BORDER)
        style.configure("TCombobox", fieldbackground=BG_ROW, foreground=FG, bordercolor=BORDER, arrowcolor=FG_MUTED)
        style.map("TCombobox", fieldbackground=[("readonly", BG_ROW)])
        style.configure("TRadiobutton", background=BG_ROW, foreground=FG_MUTED)
        style.map("TRadiobutton", background=[("active", BG_ROW)])
        style.configure("Vertical.TScrollbar", background=BG_CARD, troughcolor=BG, bordercolor=BG)

    def _build_ui(self) -> None:
        main = tk.Frame(self.root, bg=BG)
        main.pack(fill="both", expand=True, padx=16, pady=16)
        main.columnconfigure(0, weight=1)

        base_wrap = tk.Frame(main, bg=BG_CARD, highlightbackground=BORDER, highlightthickness=1)
        base_wrap.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        tk.Label(
            base_wrap,
            text="AUSGANGSLAGE & ANNAHMEN",
            bg=BG_CARD,
            fg=FG_MUTED,
            font=("SF Pro Text", 9),
        ).pack(anchor="w", padx=14, pady=(12, 4))
        base = tk.Frame(base_wrap, bg=BG_CARD)
        base.pack(fill="x", padx=14, pady=(0, 14))
        for c in range(4):
            base.columnconfigure(c, weight=1)
        fields = [
            ("BAX alt (offiziell)", self.balt),
            ("Bisherige Spiele", self.n0),
            ("Bisher SIst", self.sist0),
            ("Bisher BNiv Ø", self.bniv0),
        ]
        for i, (lab, var) in enumerate(fields):
            f = tk.Frame(base, bg=BG_CARD)
            f.grid(row=0, column=i, padx=6, sticky="ew")
            tk.Label(f, text=lab, bg=BG_CARD, fg=FG_MUTED, font=("SF Pro Text", 9)).pack(anchor="w")
            if var is self.sist0:
                ttk.Entry(f, textvariable=var, width=10).pack(anchor="w", pady=(4, 0))
            else:
                ttk.Spinbox(f, from_=0, to=9999, textvariable=var, width=10).pack(anchor="w", pady=(4, 0))
            var.trace_add("write", lambda *_: self._recalc())

        tour_head = tk.Frame(main, bg=BG)
        tour_head.grid(row=1, column=0, sticky="ew", pady=(0, 8))
        tk.Label(
            tour_head,
            text="TURNIERPLAN – FELD ANPASSEN & ERGEBNIS SIMULIEREN",
            bg=BG,
            fg=FG,
            font=("SF Pro Text", 11, "bold"),
        ).pack(side="left")
        ttk.Button(tour_head, text="+ Turnier hinzufügen", command=self._add_tournament).pack(side="right")

        canvas = tk.Canvas(main, highlightthickness=0, height=340, bg=BG, bd=0)
        scroll = ttk.Scrollbar(main, orient="vertical", command=canvas.yview)
        self.tour_inner = tk.Frame(canvas, bg=BG)
        self.tour_inner.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
        )
        canvas.create_window((0, 0), window=self.tour_inner, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.grid(row=2, column=0, sticky="nsew", pady=(0, 12))
        scroll.grid(row=2, column=1, sticky="ns")
        main.rowconfigure(2, weight=1)

        def _on_mousewheel(event: tk.Event) -> str:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            return "break"

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        out = tk.Frame(main, bg=BG)
        out.grid(row=3, column=0, columnspan=2, sticky="ew")
        out.columnconfigure(0, weight=1)

        erg_wrap = tk.Frame(out, bg=BG_CARD, highlightbackground=BORDER, highlightthickness=1)
        erg_wrap.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        tk.Label(
            erg_wrap,
            text="ERGEBNIS",
            bg=BG_CARD,
            fg=FG_MUTED,
            font=("SF Pro Text", 9),
        ).pack(anchor="w", padx=14, pady=(12, 8))
        self.summary_fr = tk.Frame(erg_wrap, bg=BG_CARD)
        self.summary_fr.pack(fill="x", padx=14, pady=(0, 8))
        self._build_summary_metrics()

        self.footer_lbl = tk.Label(
            erg_wrap,
            text="",
            bg=BG_CARD,
            fg=FG_MUTED,
            font=("SF Pro Text", 10),
            wraplength=780,
            justify="left",
        )
        self.footer_lbl.pack(fill="x", padx=14, pady=(0, 14))

        self.rec_lbl = tk.Label(
            out,
            wraplength=780,
            justify="left",
            bg=BG,
            fg=FG_MUTED,
            font=("SF Pro Text", 10),
        )
        self.rec_lbl.grid(row=2, column=0, sticky="w")

        self._add_tournament()

    def _build_summary_metrics(self) -> None:
        if self._summary_metrics_built:
            return
        self._metric_neuer = tk.StringVar(value="—")
        self._metric_delta = tk.StringVar(value="—")
        self._metric_spiele = tk.StringVar(value="—")
        self._metric_bniv = tk.StringVar(value="—")
        self._metric_berst = tk.StringVar(value="—")
        self._metric_bn = tk.StringVar(value="—")

        titles = (
            ("Neuer BAX", self._metric_neuer, ACCENT_BLUE),
            ("Veränderung", self._metric_delta, ACCENT_GREEN),
            ("Gesamtspiele", self._metric_spiele, FG),
            ("BNiv (Ø Gegner)", self._metric_bniv, FG),
            ("Berst", self._metric_berst, FG),
            ("Bn", self._metric_bn, FG),
        )
        for i, (title, var, color) in enumerate(titles):
            r, c = divmod(i, 3)
            card = tk.Frame(self.summary_fr, bg=BG_ROW, highlightbackground=BORDER, highlightthickness=1)
            card.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
            self.summary_fr.columnconfigure(c, weight=1)
            tk.Label(card, text=title, bg=BG_ROW, fg=FG, font=("SF Pro Text", 9)).pack(anchor="w", padx=12, pady=(10, 4))
            val_lbl = tk.Label(
                card,
                textvariable=var,
                bg=BG_ROW,
                fg=color,
                font=("SF Pro Text", 20, "bold"),
            )
            val_lbl.pack(anchor="w", padx=12, pady=(0, 12))
            if i == 1:
                self._lbl_delta_metric = val_lbl
        self._summary_metrics_built = True

    def _add_tournament(self) -> None:
        idx = len(self.tournaments)
        block = TournamentBlock(
            self.tour_inner,
            idx,
            on_change=self._recalc,
            remove_cb=self._remove_tournament,
        )
        block.name_var.set(f"Turnier {idx + 1}")
        block.outer.pack(fill="x", pady=(0, 8))
        self.tournaments.append(block)
        self._recalc()

    def _remove_tournament(self, block: TournamentBlock) -> None:
        if len(self.tournaments) <= 1:
            return
        self.tournaments.remove(block)
        block.destroy()
        for i, t in enumerate(self.tournaments):
            t.set_index(i)
        self._recalc()

    def _parse_float(self, v: tk.Variable, default: float) -> float:
        try:
            return float(str(v.get()).replace(",", "."))
        except (tk.TclError, ValueError):
            return default

    def _recalc(self) -> None:
        if self._recalc_after_id is not None:
            self.root.after_cancel(self._recalc_after_id)
        self._recalc_after_id = self.root.after(self._debounce_ms, self._recalc_impl)

    def _recalc_impl(self) -> None:
        self._recalc_after_id = None
        balt = float(self.balt.get())
        n0 = int(self.n0.get()) if str(self.n0.get()).strip() else 0
        bniv0 = float(self.bniv0.get())
        sist0 = self._parse_float(self.sist0, 0.0)

        steps_data: List[tuple] = []
        for t in self.tournaments:
            s = t.build_step()
            if s is None:
                continue
            steps_data.append(s)

        res = simulate_from_base(balt, n0, bniv0, sist0, steps_data)
        self._render_summary(res, balt, bniv0, n0, sist0)
        self._update_tournament_row_bax(res)

    def _update_tournament_row_bax(self, res: SimulationResult) -> None:
        step_i = 0
        for t in self.tournaments:
            s = t.build_step()
            if s is None:
                t.set_row_bax(None, None)
                continue
            if step_i >= len(res.steps):
                t.set_row_bax(None, None)
                continue
            st = res.steps[step_i]
            prev_bax = res.b_start if step_i == 0 else res.steps[step_i - 1].bneu
            delta = st.bneu - prev_bax
            t.set_row_bax(st.bneu, delta)
            step_i += 1

    def _render_summary(
        self,
        res: SimulationResult,
        balt: float,
        bniv0: float,
        n0: int,
        sist0: float,
    ) -> None:
        last = res.steps[-1] if res.steps else None
        final_bax = last.bneu if last else res.b_start
        total_n = last.cum_n if last else res.initial_cum_n

        delta_vs_alt = final_bax - balt
        self._metric_neuer.set(f"{final_bax:.0f}")
        dtxt = f"{delta_vs_alt:+.0f}"
        self._metric_delta.set(dtxt)
        self._lbl_delta_metric.configure(fg=ACCENT_GREEN if delta_vs_alt >= 0 else ACCENT_RED)
        self._metric_spiele.set(f"{total_n:.0f}")

        if last:
            self._metric_bniv.set(f"{last.bniv_now:.1f}")
            self._metric_berst.set(f"{last.berst:.1f}")
            self._metric_bn.set(f"{last.bn:.1f}")
        else:
            cum_ssoll0 = n0 * gew(balt, bniv0)
            _, berst0, bn0v = calc_bneu(balt, bniv0, float(n0), sist0, cum_ssoll0)
            self._metric_bniv.set(f"{bniv0:.1f}")
            self._metric_berst.set(f"{berst0:.1f}")
            self._metric_bn.set(f"{bn0v:.1f}")

        if res.steps:
            tg = sum(st.n for st in res.steps)
            tw = sum(st.wins for st in res.steps)
            tl = sum(st.losses for st in res.steps)
            w_avg = sum(st.avg_bax * st.n for st in res.steps) / tg if tg else 0.0
            self.footer_lbl.configure(
                text=f"{tg}× Gegner-BAX Ø {w_avg:.0f}, {tw} Siege, {tl} Niederlagen"
            )
        else:
            self.footer_lbl.configure(text="")

        self.rec_lbl.configure(text=recommendation_text(final_bax))

    def _draw_chart(self, res: SimulationResult) -> None:
        w = int(self.chart.winfo_width() or 700)
        h = int(self.chart.winfo_height() or 200)
        if w < 10:
            w = 700
        if h < 10:
            h = 200
        key = tuple(res.history_bax)
        if (
            key == self._last_chart_key
            and (w, h) == self._last_chart_wh
            and len(res.history_bax) >= 2
        ):
            return
        self._last_chart_key = key
        self._last_chart_wh = (w, h)

        self.chart.delete("all")

        vals = res.history_bax
        if len(vals) < 2:
            self.chart.create_text(
                w // 2,
                h // 2,
                text="Mehrere Turniere mit Ergebnis eintragen für den Verlauf.",
                fill=FG_DIM,
                font=("SF Pro Text", 11),
            )
            return

        ymin, ymax = min(vals), max(vals)
        pad = max(5, (ymax - ymin) * 0.15)
        y0, y1 = ymin - pad, ymax + pad
        if y1 <= y0:
            y1 = y0 + 1

        left, right, top, bot = 48, w - 12, 14, h - 28

        def x_of(i: int) -> float:
            n = len(vals) - 1
            return left + (right - left) * (i / n) if n else left

        def y_of(v: float) -> float:
            return top + (bot - top) * (1 - (v - y0) / (y1 - y0))

        for yv, dash in ((480, (4, 4)), (490, (2, 4))):
            if y0 <= yv <= y1:
                yy = y_of(yv)
                self.chart.create_line(left, yy, right, yy, fill="#378ADD", dash=dash)

        pts: List[float] = []
        for i, v in enumerate(vals):
            pts.extend([x_of(i), y_of(v)])

        if len(pts) >= 4:
            self.chart.create_line(*pts, fill=ACCENT_GREEN, width=2, smooth=True)
        for i, v in enumerate(vals):
            self.chart.create_oval(
                x_of(i) - 3,
                y_of(v) - 3,
                x_of(i) + 3,
                y_of(v) + 3,
                fill=ACCENT_GREEN,
                outline="",
            )

        self.chart.create_text(
            8,
            (top + bot) / 2,
            text="BAX",
            angle=90,
            fill=FG_DIM,
            font=("SF Pro Text", 9),
        )
        for i, lab in enumerate(res.history_labels):
            self.chart.create_text(
                x_of(i),
                h - 12,
                text=lab[:10],
                fill=FG_MUTED,
                font=("SF Pro Text", 8),
            )

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    TurnierplanApp().run()


if __name__ == "__main__":
    main()
