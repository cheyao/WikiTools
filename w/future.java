package com.cyao.theconverter.worlds;

import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.Regex;

@Metadata(mo3720d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004J\u0006\u0010\u0007\u001a\u00020\u0003R\u0011\u0010\u0002\u001a\u00020\u0003¢\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006¨\u0006\b"}, mo3721d2 = {"Lcom/cyao/theconverter/worlds/future;", "", "last", "", "(Ljava/lang/String;)V", "getLast", "()Ljava/lang/String;", "future1", "app_debug"}, mo3722k = 1, mo3723mv = {1, 6, 0}, mo3725xi = 48)
/* compiled from: future.kt */
public final class future {
    private final String last;

    public future(String last2) {
        Intrinsics.checkNotNullParameter(last2, "last");
        this.last = last2;
    }

    public final String getLast() {
        return this.last;
    }

    public final String future1() {
        Regex regex = new Regex("\\s*\\(future" + "@ZombieTypes" + "\\)\\s*");
        Regex regex2 = new Regex("\\s*\\(future_armor1" + "@ZombieTypes" + "\\)\\s*");
        Regex regex3 = new Regex("\\s*\\(future_armor2" + "@ZombieTypes" + "\\)\\s*");
        Regex regex4 = new Regex("\\s*\\(future_jetpack" + "@ZombieTypes" + "\\)\\s*");
        Regex regex5 = new Regex("\\s*\\(future_protector" + "@ZombieTypes" + "\\)\\s*");
        Regex regex6 = new Regex("\\s*\\(mech_cone" + "@ZombieTypes" + "\\)\\s*");
        Regex regex7 = new Regex("\\s*\\(disco_mech" + "@ZombieTypes" + "\\)\\s*");
        Regex regex8 = new Regex("\\s*\\(future_jetpack_disco" + "@ZombieTypes" + "\\)\\s*");
        Regex regex9 = new Regex("\\s*\\(football_mech" + "@ZombieTypes" + "\\)\\s*");
        Regex regex10 = new Regex("\\s*\\(future_gargantuar" + "@ZombieTypes" + "\\)\\s*");
        return new Regex("\\s*\\(future_imp" + "@ZombieTypes" + "\\)\\s*").replace((CharSequence) regex10.replace((CharSequence) regex9.replace((CharSequence) regex8.replace((CharSequence) regex7.replace((CharSequence) regex6.replace((CharSequence) regex5.replace((CharSequence) regex4.replace((CharSequence) regex3.replace((CharSequence) regex2.replace((CharSequence) regex.replace((CharSequence) this.last, "105 \\{\\{Future Zombie|2}}"), "106 \\{\\{Future Conehead Zombie|2}}"), "107 \\{\\{Future Buckethead Zombie|2}}"), "111 \\{\\{Jetpack Zombie|2}}"), "110 \\{\\{Shield Zombie|2}}"), "112 \\{\\{Robo-Cone Zombie|2}}"), "113 \\{\\{Disco-tron 3000|2}}"), "114 \\{\\{Disco Jetpack Zombie|2}}"), "115 \\{\\{Mecha-Football Zombie|2}}"), "108 \\{\\{Gargantuar Prime|2}}"), "109 \\{\\{Bug Bot Imp|2}}");
    }
}
